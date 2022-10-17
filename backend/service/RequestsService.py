import threading
from typing import Any, List, Dict
import os

import requests
import bs4 as bs
from bs4 import NavigableString
from requests import Response

from backend.model.ChapterContent import ChapterContent
from config import resource_path
from backend.model.NovelBasicInfo import NovelBasicInfo
from backend.model.ChapterBasicInfo import ChapterBasicInfo
from backend.model.NovelDisplayInfo import NovelDisplayInfo

from backend.utils.LoggingConfiger import logger
from backend.utils.IntervalTimeCaculator import IntervalTimeCaculator


# 爬虫相关的服务,由于网络io操作不确定性大，不交给dao了
# 需要获得的信息：小说url -> （小说名，小说封面，小说最新更新的时间），(章节总数)，(章节名，章节网址，章节索引）*初始化时
#              章节url -> (章节内容) *选择了某部小说时


class RequestThread(threading.Thread):
    def __init__(self, func, name="a thread", args=()):
        super().__init__()
        self.func = func
        self.name = name
        self.args = args
        self.result = None

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self) -> Response or None:
        if not self.result:
            logger.warning("爬虫任务超时或出错")
        return self.result


class RequestsService:

    def get_html_thread(self, url: str) -> Response or None:
        try:
            return requests.get(url)
        except requests.exceptions.MissingSchema:
            logger.error("不标准的URL")
        except Exception:
            logger.error("爬虫发生了未知错误")

    def get_html_by_url(self, url: str) -> str or None:
        t = RequestThread(self.get_html_thread, name="RequestThread", args=[url])
        t.start()

        time = IntervalTimeCaculator()
        time.start()
        logger.info("开始爬取html信息...")

        # 3秒还没拿到，基本凉了
        t.join(timeout=5)

        time.end()

        r = t.get_result()

        if not r:
            # 任务超时或者出错
            logger.warning("html爬取失败")
            return None
        else:
            logger.info("html爬取完毕，花费 %f 秒" % time.get_interval_time())

        if r.status_code != 200:
            logger.info("错误的响应码")
            return None

        return r.text

    def get_novel_display_infos_by_objects(self, l: List[NovelBasicInfo]) -> List[NovelDisplayInfo] or None:
        res = []

        time = IntervalTimeCaculator()
        time.start()
        logger.info("开始批量爬虫...")

        for o in l:
            n = self.get_novel_display_info_by_object(o)
            if not n:
                time.end()
                logger.warning("任务出错，已中断批量爬虫, 花费 %f 秒" % time.get_interval_time())
                return None
            res.append(n)

        time.end()
        logger.info("批量爬虫结束，花费 %f 秒" % time.get_interval_time())

        return res

    def get_novel_display_info_by_object(self, o: NovelBasicInfo) -> NovelDisplayInfo or None:
        return self.get_novel_display_info_by_id_and_url(o.id, o.url)

    # 不同网站处理不同，总之实现接口就行了
    def get_novel_display_info_by_id_and_url(self, id: int, url: str) -> NovelDisplayInfo or None:
        r = self.get_html_by_url(url)

        if not r:
            return None

        html = bs.BeautifulSoup(r, features="lxml")

        # 根据不同网站进行不同处理
        if url.__contains__("https://www.qb5.tw/"):
            return self.get_novel_display_info_by_html_with_qb5tw(html, id)
        elif url.__contains__("https://www.xbiquge.la/"):
            return self.get_novel_display_info_by_html_with_xbiquge(html, id)

    def get_novel_display_info_by_html_with_qb5tw(self, html: bs.BeautifulSoup, id: int) -> NovelDisplayInfo:
        book_detail = html.find("div", attrs={"id": "bookdetail"})

        # 小说名
        name = book_detail.find("h1").contents[0]

        # 小说封面(需要下载),有点慢
        cover_url = book_detail.find("img").get("src")
        cover_path = resource_path.NOVEL_COVERS_DIRECTORY + name + ".jpg"

        self.download_image_to_resouce_by_url(cover_url, cover_path)

        return NovelDisplayInfo(id, name, cover_path, 0, "还没看过")

    def get_novel_display_info_by_html_with_xbiquge(self, html: bs.BeautifulSoup, id: int) -> NovelDisplayInfo:
        book_detail = html.find("div", attrs={"class": "box_con"})

        info = book_detail.find("div", attrs={"id": "info"})

        # 小说名
        name = info.find("h1").text

        # 封面
        cover_url = book_detail.find("div", attrs={"id": "fmimg"}).find("img").get("src")
        cover_path = resource_path.NOVEL_COVERS_DIRECTORY + name + ".jpg"

        self.download_image_to_resouce_by_url(cover_url, cover_path)

        return NovelDisplayInfo(id, name, cover_path, 0, "还没看过")

    def get_chapter_basic_infos_by_object(self, o: NovelBasicInfo) -> List[ChapterBasicInfo] or None:
        return self.get_chapter_basic_infos_by_id_and_url(o.id, o.url)

    def get_chapter_basic_infos_by_id_and_url(self, id: int, url: str) -> List[ChapterBasicInfo] or None:
        r = self.get_html_by_url(url)

        if not r:
            return None

        html = bs.BeautifulSoup(r, features="lxml")

        if url.__contains__("https://www.qb5.tw/"):
            return self.get_chapter_basic_infos_by_html_with_qb5tw(html, id, url)

    def get_chapter_basic_infos_by_html_with_qb5tw(self, html: bs.BeautifulSoup, id: int, url: str) -> List[ChapterBasicInfo]:
        l= html.find("dl", attrs={"class": "zjlist"}).find_all("dd")

        return self.get_chapter_basic_infos_by_list_with_qb5tw(l, id, url)

    def get_chapter_basic_infos_by_list_with_qb5tw(self, l: Any, id: int, url: str) -> List[ChapterBasicInfo]:
        r = []
        index = 0
        for i in range(len(l)):
            o = l[i].find("a")

            if not o:
                logger.warning("当前小说索引为%d的章节信息缺失，默认不获取" % i)
                continue

            r.append(ChapterBasicInfo(id, o.text, index, url + o.get("href")))
            index += 1
        return r

    # 拿到某部小说在软件初始化时需要的全部两个对象
    def get_all_init_needy_objects_by_object(self, o: NovelBasicInfo) -> Dict[type, object] or None:
        time = IntervalTimeCaculator()
        time.start()
        logger.info("开始爬取某部小说初始化需要的全部两个对象...")

        url = o.url

        r = self.get_html_by_url(url)

        if not r:
            logger.warning("爬虫失败，任务已中断")
            return None

        html = bs.BeautifulSoup(r, features="lxml")

        d = {}

        if url.__contains__("https://www.qb5.tw/"):
            r1 = self.get_novel_display_info_by_html_with_qb5tw(html, o.id)

            if not r1:
                logger.warning("爬虫失败，任务已中断")
                return

            d[NovelDisplayInfo] = r1

            l = html.find("dl", attrs={"class": "zjlist"}).find_all("dd")

            r3 = self.get_chapter_basic_infos_by_list_with_qb5tw(l, o.id, o.url)

            if not r3:
                logger.warning("爬虫失败，任务已中断")
                return

            d[ChapterBasicInfo] = r3

            time.end()
            logger.info("某部小说初始化需要的全部两个对象爬取完毕，花费 %f 秒" % time.get_interval_time())

            return d

    def get_object_by_type_and_object(self, t: type, o: NovelBasicInfo) -> object or None:
        if t == NovelDisplayInfo:
            return self.get_novel_display_info_by_object(o)
        elif t == ChapterBasicInfo:
            return self.get_chapter_basic_infos_by_object(o)

    def get_object_by_type_and_html_with_qb5tw(self, t: type, html: bs.BeautifulSoup, o: NovelBasicInfo) -> object or None:
        if t == NovelDisplayInfo:
            return self.get_novel_display_info_by_html_with_qb5tw(html, o.id)
        elif t == ChapterBasicInfo:
            return self.get_chapter_basic_infos_by_html_with_qb5tw(html, o.id, o.url)

    # 根据给定的类型爬取数据，内部含优化 -> NovelDisplayInfo NovelAllChaptersBasicInfo ChapterBasicInfo
    def get_objects_by_types_and_object(self, l: List[type], o: NovelBasicInfo) -> Dict[type, object] or None:
        logger.info("根据给定类型爬取数据中...")
        lenth = len(l)

        if lenth > 2 or lenth <= 0:
            logger.error("给定类型数量错误")
            return

        if lenth == 2:
            return self.get_all_init_needy_objects_by_object(o)

        if lenth == 1:
            d = {}

            t = l[0]

            r = self.get_object_by_type_and_object(t, o)

            if not r:
                logger.warning("爬虫失败，任务已中断")
                return

            d[t] = r
            return d

    def download_image_to_resouce_by_url(self, url: str, path: str) -> None:
        time = IntervalTimeCaculator()
        time.start()
        logger.info("开始下载图片...")

        if os.path.exists(path):
            logger.info("图片已存在，跳过下载")
            return

        content = requests.get(url).content

        f = open(path, "wb")
        f.write(content)
        f.close()

        time.end()
        logger.info("图片下载完成，花费 %f 秒" % time.get_interval_time())

    def get_chapter_content_by_object(self, o: ChapterBasicInfo) -> ChapterContent or None:
        return self.get_chapter_content_by_id_and_url_and_index(o.id, o.url, o.index)

    def get_chapter_content_by_id_and_url_and_index(self, id: int, url: str, index: int) -> ChapterContent or None:
        r = self.get_html_by_url(url)

        if not r:
            return

        html = bs.BeautifulSoup(r, features="lxml")

        if url.__contains__("https://www.qb5.tw/"):
            return self.get_chapter_content_by_html_with_qb5tw(html, id, index)

    def get_chapter_content_by_html_with_qb5tw(self, html: bs.BeautifulSoup, id: int, index: int) -> ChapterContent or None:
        # 获取章节标题
        title = html.find("h1").text
        # 获取章节内容，分段处理
        l = []
        c = 0
        contents = html.find("div", attrs={"id": "content"}).contents

        for i in range(3, len(contents)):
            o = contents[i]

            if type(o) == NavigableString:
                c += len(o)
                l.append(o[5:])

        return ChapterContent(id, index, c, title, l)

    def get_name_and_author_by_url(self, url: str) -> List[str] or None:
        logger.info("爬取添加小说需要的信息...")

        if url.__contains__("https://www.qb5.tw/"):
            return self.get_name_and_author_by_url_with_qb5tw(url)
        else:
            logger.warning("爬取失败")

    def get_name_and_author_by_url_with_qb5tw(self, url: str) -> List[str] or None:
        r = self.get_html_by_url(url)

        if not r:
            return

        html = bs.BeautifulSoup(r, features="lxml")

        book_detail = html.find("div", attrs={"id": "bookdetail"})

        h1 = book_detail.find("h1")

        name = h1.contents[0]

        author = h1.find("a").text

        logger.info("爬取成功")

        return [name, author]


requests_service = RequestsService()


if __name__ == "__main__":
    n = RequestsService()
    n.get_novel_display_info_by_id_and_url(41, "https://www.xbiquge.la/7/7194/")
    pass



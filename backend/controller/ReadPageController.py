from typing import List

from backend.model.ChapterBasicInfo import ChapterBasicInfo
from backend.model.ChapterContent import ChapterContent
from backend.model.NovelBasicInfo import NovelBasicInfo
from backend.model.NovelDisplayInfo import NovelDisplayInfo
from backend.service.NovelReadService import NovelReadService
from backend.service.NovelReadService import novel_read_service
from backend.service.NovelDisplayService import NovelDisplayService
from backend.service.NovelDisplayService import novel_display_service
from backend.service.RequestsService import RequestsService
from backend.service.RequestsService import requests_service
from backend.service.CacheService import CacheService
from backend.service.CacheService import cache_service
from backend.utils.LoggingConfiger import logger
from backend.utils.IntervalTimeCaculator import IntervalTimeCaculator


class ReadPageController:

    def __init__(self):
        self.read_page_service   : NovelReadService                   = novel_read_service
        self.display_page_service: NovelDisplayService                = novel_display_service
        self.requests_service    : RequestsService                    = requests_service
        self.cache_service       : CacheService                       = cache_service

    def get_chapter_basic_info_by_display_object(self, o: NovelDisplayInfo) -> ChapterBasicInfo or None:
        return self.read_page_service.get_chapter_basic_info_by_object_from_cache(o)

    def get_chapter_basic_info_by_id_and_index(self, id: int, index: int) -> ChapterBasicInfo or None:
        return self.read_page_service.get_chapter_basic_info_by_id_and_index_from_cache(id, index)

    def get_chapter_basic_infos_by_id(self, id: int) -> List[ChapterBasicInfo] or None:
        return self.read_page_service.get_chapter_basic_infos_by_id_from_cache(id)

    def get_chapter_basic_infos_by_basic_object(self, o: NovelBasicInfo) -> List[ChapterBasicInfo] or None:
        # 实际上，此类数据会比较庞大，不太推荐存到json里，最好存进真正的数据库，出现效率问题首先考虑这个
        chapter_basic_infos = self.read_page_service.get_chapter_basic_infos_by_id_from_cache(o.id)

        return chapter_basic_infos

    def get_chapter_content_by_object(self, o: ChapterBasicInfo) -> ChapterContent or None:
        time = IntervalTimeCaculator()
        time.start()
        logger.info("开始爬取给定小说章节内容...")

        chapter_content = self.requests_service.get_chapter_content_by_object(o)

        if not chapter_content:
            logger.warning("爬虫失败，任务已中断")
            return None

        return chapter_content

    def im_reading_the_id_and_index_of(self, id: int, index: int):
        self.cache_service.im_reading_the_id_of(id)
        self.cache_service.im_reading_the_index_of(index)

    def is_read_page_need_to_reload(self, id: int, index: int):
        return self.the_id_im_reading() != id or self.the_index_im_reading() != index

    def the_id_im_reading(self):
        return self.cache_service.cur_read_id

    def the_index_im_reading(self):
        return self.cache_service.cur_read_index

    def put_last_saw_index_to_cache(self):
        self.cache_service.changed_last_saw_index_to_cache()

    def put_last_update_time_by_id_to_cache(self, id: int, last_update_time: str):
        self.display_page_service.put_last_update_time_by_id_to_cache(id, last_update_time)


read_page_controller = ReadPageController()


if __name__ == "__main__":
    n = ReadPageController()
    i = NovelBasicInfo(1, "https://www.qb5.tw/book_79575/")
    j = NovelBasicInfo(2, "https://www.qb5.tw/book_44997/")


from backend.model.ChapterBasicInfo import ChapterBasicInfo
from backend.model.NovelBasicInfo import NovelBasicInfo
from backend.model.NovelDisplayInfo import NovelDisplayInfo
from backend.service.NovelDisplayService import NovelDisplayService, novel_display_service
from backend.service.NovelReadService import NovelReadService, novel_read_service
from backend.service.RequestsService import RequestsService, requests_service
from backend.utils.IntervalTimeCaculator import IntervalTimeCaculator
from backend.utils.LoggingConfiger import logger


class InitController:

    def __init__(self):
        self.requests_service     : RequestsService                     = requests_service
        self.display_page_service : NovelDisplayService                  = novel_display_service
        self.read_page_service    : NovelReadService                     = novel_read_service

    # 一次性把小说基本信息，小说展示信息，小说全部章节基本信息，小说全部章节具体信息初始化好(缓存和数据库都有)，因为它们可以通过同一个网页获取，分开效率低
    def init_all_novels_needy_data(self):
        time = IntervalTimeCaculator()
        time.start()
        logger.info("开始初始化所有小说信息...")

        novel_basic_infos = self.display_page_service.get_novel_basic_infos_from_cache()

        # 可以多线程，但需要同步
        for o in novel_basic_infos.values():
            self.init_a_novel_needy_data_by_object(o)

        time.end()
        logger.info("所有小说信息初始化完毕，花费 %f 秒" % time.get_interval_time())

    # 初始化某一部小说
    def init_a_novel_needy_data_by_object(self, o: NovelBasicInfo):
        logger.info("开始初始化id为%d的小说..." % o.id)

        novel_display_info = self.display_page_service.get_novel_display_info_by_object_from_cache(o)

        chapter_basic_infos = self.read_page_service.get_chapter_basic_infos_by_object_from_cache(o)

        missing_object = []

        if not novel_display_info:
            missing_object.append(NovelDisplayInfo)
        if not chapter_basic_infos:
            missing_object.append(ChapterBasicInfo)

        if len(missing_object) > 0:
            logger.info("小说缺失了信息，爬虫获取中...")

            d = self.requests_service.get_objects_by_types_and_object(missing_object, o)

            if not d:
                logger.warning("小说缺失信息获取失败")
                return
            # 持久化
            for t, value in d.items():
                if t == NovelDisplayInfo:
                    self.display_page_service.put_novel_display_info_to_db(value)
                elif t == ChapterBasicInfo:
                    self.read_page_service.put_chapter_basic_infos_to_db(value)
        else:
            logger.info("小说信息完整，无需爬虫")


init_controller = InitController()
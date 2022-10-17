from backend.service.RequestsService import requests_service
from backend.service.NovelDisplayService import novel_display_service
from backend.model.NovelBasicInfo import NovelBasicInfo
from backend.utils.UniqueIDGenerator import UniqueIDGenerator
from backend.service.CacheService import cache_service


class AddController:

    def add_novel_by_url(self, url: str) -> NovelBasicInfo or None:
        l = requests_service.get_name_and_author_by_url(url)

        if not l:
            return None

        id = UniqueIDGenerator.generate_by_name_and_author(l[0], l[1])

        o = NovelBasicInfo(id, url)
        novel_display_service.put_novel_basic_info_to_db(o)

        # 显然，数据库全部改变了，展示页面也要重新展示
        cache_service.changed_novel_basic_info_db()
        cache_service.changed_novel_display_info_db()
        cache_service.changed_chapter_basic_info_db()

        cache_service.changed_display_page()

        return o


add_controller = AddController()
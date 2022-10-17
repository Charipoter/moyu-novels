from typing import Dict
from backend.model.NovelBasicInfo import NovelBasicInfo
from backend.model.NovelDisplayInfo import NovelDisplayInfo
from backend.service.RequestsService import RequestsService
from backend.service.RequestsService import requests_service
from backend.service.NovelDisplayService import NovelDisplayService
from backend.service.NovelDisplayService import novel_display_service
from backend.service.NovelReadService import NovelReadService
from backend.service.NovelReadService import novel_read_service
from backend.service.CacheService import CacheService
from backend.service.CacheService import cache_service

from backend.utils.LoggingConfiger import logger


class DisplayPageController:

    def __init__(self):
        self.requests_service     : RequestsService                      = requests_service
        self.display_page_service : NovelDisplayService                  = novel_display_service
        self.read_page_service    : NovelReadService                     = novel_read_service
        self.cache_service        : CacheService                         = cache_service

    def get_novel_basic_infos(self) -> Dict[int, NovelBasicInfo] or None:
        # 优先读取缓存里的
        novel_basic_infos = self.display_page_service.get_novel_basic_infos_from_cache()

        return novel_basic_infos

    def get_novel_display_infos(self) -> Dict[int, NovelDisplayInfo] or None:
        novel_display_infos = self.display_page_service.get_novel_display_infos_from_cache()

        return novel_display_infos

    def delete_novel_by_id_from_cache(self, id: int):
        self.display_page_service.delete_novel_basic_info_by_id_from_cache(id)
        cache_service.changed_novel_basic_info_db()

        self.display_page_service.delete_novel_cover_by_id_from_resource(id)
        self.display_page_service.delete_novel_display_info_by_id_from_cache(id)
        cache_service.changed_novel_display_info_db()

        self.read_page_service.delete_chapter_basic_infos_by_id_from_cache(id)
        cache_service.changed_chapter_basic_info_db()

    def is_display_page_need_to_reload_(self):
        return self.cache_service.is_display_page_changed

    def display_page_is_loaded(self):
        self.cache_service.is_display_page_changed = False

    def display_page_need_to_reload(self):
        self.cache_service.is_display_page_changed = True
        # 数据库显然变了
        self.cache_service.changed_novel_display_info_db()


display_page_controller = DisplayPageController()


if __name__ == "__main__":
    n = DisplayPageController()
    n.get_novel_basic_infos()
    n.get_novel_display_infos()
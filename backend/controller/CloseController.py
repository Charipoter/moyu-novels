from backend.service.CloseService import close_service
from backend.service.CacheService import cache_service


class CloseController:

    # 将缓存数据库进行持久化
    def before_close(self):
        if cache_service.is_novel_basic_info_db_changed:
            close_service.persistant_novel_basic_db()
        if cache_service.is_novel_display_info_db_changed:
            close_service.persistant_novel_display_info_db()
        if cache_service.is_chapter_basic_info_db_changed:
            close_service.persistent_chapter_basic_info_db()


close_controller = CloseController()
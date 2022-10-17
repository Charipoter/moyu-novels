from backend.dao.NovelDisplayInfoDao import novel_display_info_dao
from backend.dao.NovelBasicInfoDao import novel_basic_info_dao
from backend.dao.ChapterBasicInfoDao import chapter_basic_info_dao


class CloseService:

    def persistant_novel_basic_db(self):
        novel_basic_info_dao.persistant_cache()

    def persistant_novel_display_info_db(self):
        novel_display_info_dao.persistent_cache()

    def persistent_chapter_basic_info_db(self):
        chapter_basic_info_dao.persistant_cache()


close_service = CloseService()
from backend.dao.NovelDisplayInfoDao import novel_display_info_dao


class CacheService:

    def __init__(self):
        self.is_display_page_changed = True
        self.cur_read_id = -1
        self.cur_read_index = -1
        self.is_chapter_basic_info_db_changed = False
        self.is_novel_basic_info_db_changed = False
        self.is_novel_display_info_db_changed = False

    def changed_display_page(self):
        self.is_display_page_changed = True

    def unchanged_display_page(self):
        self.is_display_page_changed = False

    def im_reading_the_id_of(self, id: int):
        self.cur_read_id = id

    def im_reading_the_index_of(self, index: int):
        self.cur_read_index = index

    def changed_last_saw_index_to_cache(self):
        novel_display_info_dao.insert_index_into_cache(self.cur_read_id, self.cur_read_index)

    def changed_novel_basic_info_db(self):
        self.is_novel_basic_info_db_changed = True

    def changed_novel_display_info_db(self):
        self.is_novel_display_info_db_changed = True

    def changed_chapter_basic_info_db(self):
        self.is_chapter_basic_info_db_changed = True


cache_service = CacheService()
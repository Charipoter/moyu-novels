from typing import Dict, List
from backend.dao.ChapterBasicInfoDao import ChapterBasicInfoDao
from backend.dao.ChapterBasicInfoDao import chapter_basic_info_dao
from backend.model.ChapterBasicInfo import ChapterBasicInfo


# 相对某个具体小说而言
from backend.model.NovelBasicInfo import NovelBasicInfo
from backend.model.NovelDisplayInfo import NovelDisplayInfo


class NovelReadService:

    def __init__(self):
        self.chapter_basic_info_dao           : ChapterBasicInfoDao          = chapter_basic_info_dao

    def get_chapter_basic_infos_by_id_from_cache(self, id: int) -> List[ChapterBasicInfo] or None:
        l = self.chapter_basic_info_dao.get_chapters_by_id_from_cache(id)

        if not l:
            # 爬虫获得并持久化
            return None

        return l

    def get_chapter_basic_infos_by_object_from_cache(self, o: NovelBasicInfo) -> List[ChapterBasicInfo] or None:
        return self.get_chapter_basic_infos_by_id_from_cache(o.id)

    def get_chapter_basic_info_by_id_and_index_from_cache(self, id: int, index: int) -> ChapterBasicInfo or None:
        l = self.chapter_basic_info_dao.get_chapter_by_id_and_index_from_cache(id, index)

        if not l:
            # 爬虫获得并持久化
            return None

        return l

    def get_chapter_basic_info_by_object_from_cache(self, o: NovelDisplayInfo) -> ChapterBasicInfo or None:
        return self.get_chapter_basic_info_by_id_and_index_from_cache(o.id, o.last_saw_index)

    def put_chapter_basic_infos_to_db(self, l: List[ChapterBasicInfo]) -> None:
        self.chapter_basic_info_dao.insert_all(l)

    def put_chapter_basic_infos_to_cache(self, l: List[ChapterBasicInfo]) -> None:
        self.chapter_basic_info_dao.insert_all_into_cache(l)

    def delete_chapter_basic_infos_from_db(self) -> None:
        self.chapter_basic_info_dao.delete_all()

    def delete_chapter_basic_infos_from_cache(self) -> None:
        self.chapter_basic_info_dao.delete_all_from_cache()

    def delete_chapter_basic_infos_by_id_from_cache(self, id: int) -> None:
        self.chapter_basic_info_dao.delete_by_id_from_cache(id)

    def delete_chapter_basic_infos_by_id_from_db(self, id: int) -> None:
        self.chapter_basic_info_dao.delete_by_id(id)


novel_read_service = NovelReadService()


if __name__ == "__main__":
    n = NovelReadService()
    n.delete_chapter_basic_infos_from_db()
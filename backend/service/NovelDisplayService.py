import os
from typing import Dict, List

from backend.dao.NovelBasicInfoDao import NovelBasicInfoDao
from backend.dao.NovelBasicInfoDao import novel_basic_info_dao
from backend.dao.NovelDisplayInfoDao import NovelDisplayInfoDao
from backend.dao.NovelDisplayInfoDao import novel_display_info_dao
from backend.model.NovelBasicInfo import NovelBasicInfo
from backend.model.NovelDisplayInfo import NovelDisplayInfo
from backend.utils.LoggingConfiger import logger
from config import resource_path


# 注：所有dao内get相关的功能都是只和内存数据库交互的，不涉及io，放心使用（此程序内存数据库同步优先级>外部数据库）
class NovelDisplayService:

    def __init__(self):
        self.novel_basic_info_dao             : NovelBasicInfoDao            = novel_basic_info_dao
        self.novel_display_info_dao           : NovelDisplayInfoDao          = novel_display_info_dao

    def get_novel_basic_infos_from_cache(self) -> Dict[int, NovelBasicInfo] or None:
        l = self.novel_basic_info_dao.get_all_from_cache()

        # 基本不可能
        if not l:
            pass

        d = {}

        for item in l:
            d[item.id] = item

        return d

    def get_novel_display_infos_from_cache(self) -> Dict[int, NovelDisplayInfo] or None:
        l = self.novel_display_info_dao.get_all_from_cache()

        if not l:
            # 爬虫爬下来并且持久化
            return None

        d = {}

        for item in l:
            d[item.id] = item

        return d

    def get_novel_basic_info_by_object_from_cache(self, o: NovelDisplayInfo) -> NovelBasicInfo or None:
        return self.novel_basic_info_dao.get_by_id_from_cache(o.id)

    def get_novel_display_info_by_object_from_cache(self, o: NovelBasicInfo) -> NovelDisplayInfo or None:
        return self.novel_display_info_dao.get_by_id_from_cache(o.id)

    def delete_novel_basic_info_by_id_from_db(self, id: int) -> None:
        self.novel_basic_info_dao.delete_by_id(id)

    def delete_novel_basic_info_by_id_from_cache(self, id: int) -> None:
        self.novel_basic_info_dao.delete_by_id_from_cache(id)

    def delete_novel_display_infos_from_db(self) -> None:
        self.novel_display_info_dao.delete_all()

    def delete_novel_display_infos_from_cache(self) -> None:
        self.novel_display_info_dao.delete_all_from_cache()

    def delete_novel_display_info_by_id_from_db(self, id: int) -> None:
        self.novel_display_info_dao.delete_by_id(id)

    def delete_novel_display_info_by_id_from_cache(self, id: int) -> None:
        self.novel_display_info_dao.delete_by_id_from_cache(id)

    def delete_novel_covers_from_resource(self) -> None:
        path = resource_path.NOVEL_COVERS_DIRECTORY
        l = os.listdir(path)
        for name in l:
            os.remove(path + name)

    def delete_novel_cover_by_id_from_resource(self, id: int) -> None:
        o = self.novel_display_info_dao.get_by_id_from_cache(id)
        try:
            os.remove(o.cover_path)
        except FileNotFoundError:
            # 小说封面出现问题
            logger.error("小说封面文件不存在")
            return

    def put_novel_display_info_to_db(self, o: NovelDisplayInfo) -> None:
        self.novel_display_info_dao.insert(o)

    def put_novel_display_info_to_cache(self, o: NovelDisplayInfo) -> None:
        self.novel_display_info_dao.insert_into_cache(o)

    def put_novel_display_infos_to_db(self, l: List[NovelDisplayInfo]) -> None:
        self.novel_display_info_dao.insert_all(l)

    def put_novel_display_infos_to_cache(self, l: List[NovelDisplayInfo]) -> None:
        self.novel_display_info_dao.insert_all_into_cache(l)

    def put_novel_basic_info_to_cache(self, o: NovelBasicInfo) -> None:
        self.novel_basic_info_dao.insert_into_cache(o)

    def put_novel_basic_info_to_db(self, o: NovelBasicInfo) -> None:
        self.novel_basic_info_dao.insert(o)

    def put_last_update_time_by_id_to_cache(self, id: int, last_update_time: str) -> None:
        self.novel_display_info_dao.insert_last_update_time_into_cache(id, last_update_time)


novel_display_service = NovelDisplayService()


if __name__ == "__main__":
    n = NovelDisplayService()
    n.delete_novel_covers_from_resource()

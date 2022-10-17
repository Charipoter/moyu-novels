from typing import Any, List, Dict

from config import data_source_path

from backend.utils.JsonProcess import JsonProcess

from backend.model.ChapterBasicInfo import ChapterBasicInfo


class ChapterBasicInfoDao:

    def __init__(self):
        self.DATA_SOURCE: str                           = data_source_path.CHAPTER_BASIC_INFO_PATH
        self.data       : Dict[str, List[Dict]] or None = None

        self.load_json()

    def load_json(self) -> None:
        self.data = JsonProcess.load_json_as_object(self.DATA_SOURCE)

    def dump_json(self) -> None:
        JsonProcess.dump_to_json(self.data, self.DATA_SOURCE)

    def get_chapter_by_id_and_index_from_cache(self, id: int, index: int) -> ChapterBasicInfo or None:
        if not self.data.__contains__(str(id)):
            # 本小说的章节信息未被持久化
            return None

        l = self.data[str(id)]

        if index >= len(l) or index < 0:
            # 此页章节不存在
            return None

        d = l[index]

        return self.get_chapter_by_dict_from_cache(d)

    def get_chapter_by_dict_from_cache(self, d: Dict) -> ChapterBasicInfo or None:
        return ChapterBasicInfo(d["id"], d["name"], d["index"], d["url"])

    def get_chapters_by_id_from_cache(self, id: int) -> List[ChapterBasicInfo] or None:
        l = []
        if not self.data.__contains__(str(id)):
            # 本小说的章节信息未被持久化
            return None

        o = self.data[str(id)]

        for d in o:
            l.append(self.get_chapter_by_dict_from_cache(d))

        return l

    def insert(self, o: ChapterBasicInfo) -> None:
        self.insert_into_cache(o)
        self.dump_json()

    def insert_into_cache(self, o: ChapterBasicInfo) -> None:
        id = str(o.id)

        if not self.data.__contains__(id):
            # 本小说章节信息未被持久化，如若是第一章内容则创建，否则无效
            if o.index == 0:
                self.data[id] = [o.serialize()]
            return

        l = self.data[id]
        if o.index == len(l):
            # 刚好是最后一章，可以插入
            l.append(o.serialize())
            return

        if o.index >= len(l):
            # 超过本小说章节数
            return None

        l[o.index] = o.serialize()

    def insert_all(self, l: List[ChapterBasicInfo]) -> None:
        self.insert_all_into_cache(l)
        self.dump_json()

    def insert_all_into_cache(self, l: List[ChapterBasicInfo]) -> None:
        for o in l:
            self.insert_into_cache(o)

    def delete_by_id(self, id: int) -> None:
        self.delete_by_id_from_cache(id)
        self.dump_json()

    def delete_by_id_from_cache(self, id: int) -> None:
        id = str(id)

        if not self.data.__contains__(id):
            return None

        del self.data[id]

    def delete_by_id_and_index(self, id: int, index: int) -> None:
        if not self.data[str(id)]:
            return None

        l = self.data[str(id)]
        if not l:
            return None

        if index == len(l) - 1:
            del l[index]
            self.dump_json()

    def delete_by_id_and_index_from_cache(self, id: int, index: int) -> None:
        id = str(id)

        if not self.data.__contains__(id):
            return None

        l = self.data[str(id)]
        if not l:
            return None

        if index == len(l) - 1:
            del l[index]

    def delete_all_from_cache(self) -> None:
        self.data = {}

    def delete_all(self) -> None:
        self.delete_all_from_cache()
        self.dump_json()

    def persistant_cache(self) -> None:
        self.dump_json()


chapter_basic_info_dao = ChapterBasicInfoDao()


if __name__ == "__main__":
    n = ChapterBasicInfoDao()
    n.insert(ChapterBasicInfo(0,"saas",1,"sdsd"))


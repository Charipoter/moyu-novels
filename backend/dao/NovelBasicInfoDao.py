from typing import Any, List, Dict

from backend.model.NovelBasicInfo import NovelBasicInfo

from backend.utils.JsonProcess import JsonProcess

from config import data_source_path


class NovelBasicInfoDao:

    def __init__(self):
        self.DATA_SOURCE: str                     = data_source_path.NOVEL_BASIC_INFO_PATH
        self.data       : Dict[str, Dict] or None = None

        self.load_json()

    def load_json(self) -> None:
        self.data = JsonProcess.load_json_as_object(self.DATA_SOURCE)

    def dump_json(self) -> None:
        JsonProcess.dump_to_json(self.data, self.DATA_SOURCE)

    def get_by_id_from_cache(self, id: int) -> NovelBasicInfo or None:
        d = self.data[str(id)]

        # 没被持久化过(这里不可能)
        if not d:
            return None

        return NovelBasicInfo(d["id"], d["url"])

    def get_all_from_cache(self) -> List[NovelBasicInfo]:
        l = []
        for d in self.data.values():
            l.append(self.get_by_id_from_cache(d["id"]))
        return l

    def insert(self, o: NovelBasicInfo) -> None:
        self.insert_into_cache(o)
        self.dump_json()

    def insert_into_cache(self, o: NovelBasicInfo) -> None:
        id = str(o.id)
        self.data[id] = o.serialize()

    def insert_all(self, l: List[NovelBasicInfo]) -> None:
        self.insert_all_into_cache(l)
        self.dump_json()

    def insert_all_into_cache(self, l: List[NovelBasicInfo]) -> None:
        for o in l:
            id = str(o.id)
            self.data[id] = o.serialize()

    def delete_by_id(self, id: int) -> None:
        self.delete_by_id_from_cache(id)
        self.dump_json()

    def delete_by_id_from_cache(self, id: int) -> None:
        if not self.data.__contains__(str(id)):
            return
        del self.data[str(id)]

    def persistant_cache(self) -> None:
        self.dump_json()


novel_basic_info_dao = NovelBasicInfoDao()


if __name__ == "__main__":
    n = NovelBasicInfoDao()
    i = NovelBasicInfo(1,"https://www.qb5.tw/book_5324/")
    n.insert(i)

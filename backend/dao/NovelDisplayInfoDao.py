from typing import Any, List, Dict

from backend.utils.JsonProcess import JsonProcess

from backend.model.NovelDisplayInfo import NovelDisplayInfo

from config import data_source_path


class NovelDisplayInfoDao:

    def __init__(self):
        self.DATA_SOURCE: str                     = data_source_path.NOVEL_DISPLAY_INFO_PATH
        self.data       : Dict[str, Dict] or None = None

        self.load_json()

    def load_json(self) -> None:
        self.data = JsonProcess.load_json_as_object(self.DATA_SOURCE)

    def dump_json(self) -> None:
        JsonProcess.dump_to_json(self.data, self.DATA_SOURCE)

    def get_by_id_from_cache(self, id: int) -> NovelDisplayInfo or None:
        if not self.data.__contains__(str(id)):
            return

        d = self.data[str(id)]

        # 没被持久化过，最好持久化
        if not d:
            return None

        return NovelDisplayInfo(d["id"], d["name"], d["cover_path"], d["last_saw_index"], d["last_update_time"])

    def get_all_from_cache(self) -> List[NovelDisplayInfo]:
        l = []
        for d in self.data.values():
            l.append(self.get_by_id_from_cache(d["id"]))
        return l

    def insert(self, o: NovelDisplayInfo) -> None:
        self.insert_into_cache(o)
        self.dump_json()

    def insert_into_cache(self, o: NovelDisplayInfo) -> None:
        id = str(o.id)
        self.data[id] = o.serialize()

    def insert_index_into_cache(self, id: int, index: int) -> None:
        id = str(id)
        self.data[id]["last_saw_index"] = index

    def insert_index(self, id: int, index: int) -> None:
        self.insert_index_into_cache(id, index)
        self.dump_json()

    def insert_last_update_time_into_cache(self, id: int, last_update_time: str) -> None:
        id = str(id)
        self.data[id]["last_update_time"] = last_update_time

    def insert_last_update_time_into_db(self, id: int, last_update_time: str) -> None:
        self.insert_last_update_time_into_cache(id, last_update_time)
        self.dump_json()

    def insert_all(self, l: List[NovelDisplayInfo]) -> None:
        self.insert_all_into_cache(l)
        self.dump_json()

    def insert_all_into_cache(self, l: List[NovelDisplayInfo]) -> None:
        for o in l:
            self.insert_into_cache(o)

    def delete_by_id(self, id: int) -> None:
        self.delete_by_id_from_cache(id)
        self.dump_json()

    def delete_by_id_from_cache(self, id: int) -> None:
        if not self.data.__contains__(str(id)):
            return
        del self.data[str(id)]

    def delete_all_from_cache(self) -> None:
        self.data = {}

    def delete_all(self) -> None:
        self.delete_all_from_cache()
        self.dump_json()

    # 持久化缓存
    def persistent_cache(self) -> None:
        self.dump_json()


novel_display_info_dao = NovelDisplayInfoDao()


if __name__ == "__main__":
    n = NovelDisplayInfoDao()
    n.insert_all([NovelDisplayInfo(0,"奇迹的召唤师","sasasas",1,"2323"), NovelDisplayInfo(1,"sad","adsd",2,"dad")])

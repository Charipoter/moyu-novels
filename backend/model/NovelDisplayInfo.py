from typing import Dict


class NovelDisplayInfo:
    def __init__(self, id, name, cover_path, last_saw_index, last_update_time):
        # 唯一id
        self.id              : int = id
        # 小说名
        self.name            : str = name
        # 小说封面图的资源路径
        self.cover_path      : str = cover_path
        # 上一次看到的章节的索引
        self.last_saw_index  : int = last_saw_index
        # 上一次看的时间（以天为单位）
        self.last_update_time: str = last_update_time

    def __str__(self):
        return "id: %d, name: %s, cover_path: %s, last_saw_index: %d, last_update_time: %s" \
               % (self.id, self.name, self.cover_path, self.last_saw_index, self.last_update_time)

    def serialize(self) -> Dict:
        return {"id": self.id, "name": self.name, "cover_path": self.cover_path, "last_saw_index": self.last_saw_index,
                "last_update_time": self.last_update_time}




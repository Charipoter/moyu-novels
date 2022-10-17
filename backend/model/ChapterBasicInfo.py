from typing import Dict


class ChapterBasicInfo:
    def __init__(self, id, name, index, url):

        # 唯一id
        self.id   : int = id
        # 章节名
        self.name : str = name
        # 章节网址
        self.url  : str = url
        # 章节索引
        self.index: int = index

    def __str__(self):
        return "id: %d, name: %s, url: %s, index: %d" % (self.id, self.name, self.url, self.index)

    def serialize(self) -> Dict:
        return {"id": self.id, "name": self.name, "url": self.url, "index": self.index}


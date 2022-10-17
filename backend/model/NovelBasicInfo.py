from typing import Dict


class NovelBasicInfo:
    def __init__(self, id, url):
        # 唯一id
        self.id : int = id
        # 小说网址
        self.url: str = url

    def __str__(self) -> str:
        return "id: %d, url: %s" % (self.id, self.url)

    def serialize(self) -> Dict:
        return {"id": self.id, "url": self.url}
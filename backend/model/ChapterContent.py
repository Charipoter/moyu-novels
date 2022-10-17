from typing import List


class ChapterContent:

    def __init__(self, id, index, word_number, title, paragraphs):
        # 唯一id
        self.id         : int       = id
        # 在章节中的索引
        self.index      : int       = index
        # 字数
        self.word_number: int       = word_number
        # 标题
        self.title      : str       = title
        # 段落，这个形式可能有用
        self.paragraphs : List[str] = paragraphs
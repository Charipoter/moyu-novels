import os

# absolute_path = "E:\\_PYCHARM_\\PROJECT\\moyu-novels"

absolute_path = os.getcwd()


class DataSourcePath:

    def __init__(self):

        self.NOVEL_BASIC_INFO_PATH = absolute_path + "\\resource\\db\\NovelBasicInfo.json"
        self.NOVEL_DISPLAY_INFO_PATH = absolute_path + "\\resource\\db\\NovelDisplayInfo.json"
        self.CHAPTER_BASIC_INFO_PATH = absolute_path + "\\resource\\db\\ChapterBasicInfo.json"
        self.SETTING_PATH = absolute_path + "\\resource\\db\\setting.json"


data_source_path = DataSourcePath()


class ResourcePath:

    def __init__(self):

        self.NOVEL_COVERS_DIRECTORY = absolute_path + "\\resource\\novel-covers\\"
        self.BACKGROUND = absolute_path + "\\resource\\background\\"


resource_path = ResourcePath()


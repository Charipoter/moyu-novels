from PyQt5.QtWidgets import QWidget

from frontend.windows.MainWindow import MainWindow
from config import data_source_path
from backend.utils.JsonProcess import JsonProcess


class SettingFunction:

    path = data_source_path.SETTING_PATH

    setting = JsonProcess.load_json_as_object(path)

    @classmethod
    def get_font_size(cls) -> int:
        return cls.setting["font_size"]

    @classmethod
    def get_font(cls) -> int:
        return cls.setting["font"]

    @classmethod
    def get_theme(cls) -> int:
        return cls.setting["theme"]

    @classmethod
    def change_theme(cls, i):
        cls.setting["theme"] = i

    @classmethod
    def change_font(cls, i):
        cls.setting["font"] = i

    @classmethod
    def change_font_size(cls, i):
        cls.setting["font_size"] = i

    @classmethod
    def before_close(cls):
        JsonProcess.dump_to_json(cls.setting, cls.path)
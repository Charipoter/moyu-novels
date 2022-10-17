from PyQt5.QtCore import QThread, pyqtSignal

from backend.controller.AddController import add_controller
from backend.controller.DisplayPageController import display_page_controller
from backend.controller.InitController import init_controller


class AddThread(QThread):
    signal = pyqtSignal(bool)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        # 内部已调用使得展示界面要再加载
        o = add_controller.add_novel_by_url(self.url)

        if not o:
            display_page_controller.display_page_is_loaded()
            # 发送信号进行页面更新
            self.signal.emit(False)
            return
        # 初始化本小说
        init_controller.init_a_novel_needy_data_by_object(o)

        # 发送信号进行页面更新
        self.signal.emit(True)
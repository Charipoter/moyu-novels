from PyQt5.QtCore import QThread, pyqtSignal

from backend.controller.ReadPageController import read_page_controller


class ContentThread(QThread):
    signal = pyqtSignal(object)

    def __init__(self, chapter_basic_info):
        super().__init__()
        self.chapter_basic_info = chapter_basic_info

    def run(self):
        chapter_content = read_page_controller.get_chapter_content_by_object(self.chapter_basic_info)

        if chapter_content:
            # 发送信号进行页面更新
            self.signal.emit(chapter_content)
        else:
            self.signal.emit(None)
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHeaderView, QWidget

from frontend.functions.DisplayPageFunction import DisplayPageFunction
from backend.controller.InitController import init_controller
from backend.controller.CloseController import close_controller
from frontend.functions.StyleFunction import StyleFunction
from frontend.functions.ReadPageFunction import ReadPageFunction
from frontend.functions.SettingFunction import SettingFunction


class MainFunction(DisplayPageFunction, ReadPageFunction, StyleFunction):

    def __init__(self):
        super().__init__()
        init_controller.init_all_novels_needy_data()

        self.setting_container.close()
        widget = QWidget()
        widget.setMaximumHeight(0)
        self.setting_container.setTitleBarWidget(widget)

    # 程序关闭时，将缓存数据库持久化
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        close_controller.before_close()
        SettingFunction.before_close()
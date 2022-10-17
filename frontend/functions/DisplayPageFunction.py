import threading
from typing import Dict

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QMenu, QInputDialog, QLineEdit, QMessageBox, QHeaderView

from backend.model.NovelDisplayInfo import NovelDisplayInfo
from frontend.windows.MainWindow import MainWindow
from backend.controller.DisplayPageController import display_page_controller
from backend.controller.ReadPageController import read_page_controller
from backend.utils.LoggingConfiger import logger
from frontend.functions.threads.AddThread import AddThread


class DisplayWidget(QtWidgets.QWidget):

    def __init__(self, o: NovelDisplayInfo):
        super().__init__()
        self.novel_display_info = o


class DisplayPageFunction(MainWindow):

    def create_novel_display_width_by_object(self, o: NovelDisplayInfo, width, height):
        # 设计

        name = o.name
        last_saw_index = o.last_saw_index
        last_update_time = o.last_update_time
        cover_path = o.cover_path

        # 水平布局
        horizontal_layout = QtWidgets.QHBoxLayout()
        # 设置空格
        horizontal_layout.setContentsMargins(6, 3, 6, 3)

        x1 = height * 0.75
        x2 = width - x1

        cover = QPixmap(cover_path)

        cover_label = QtWidgets.QLabel()
        cover_label.setScaledContents(True)
        cover_label.setFixedWidth(x1)
        cover_label.setPixmap(cover)

        horizontal_layout.addWidget(cover_label)
        # 垂直布局
        vertical_layout = QtWidgets.QVBoxLayout()

        name_label = QtWidgets.QLabel()
        # name_label.setStyleSheet("font: 11pt \"黑体\";")
        name_label.setText(name)

        vertical_layout.addWidget(name_label)

        last_update_time_label = QtWidgets.QLabel()
        # last_update_time_label.setStyleSheet("font: 10pt \"等线\";")
        last_update_time_label.setText("⏰ " + last_update_time)

        vertical_layout.addWidget(last_update_time_label)

        last_saw_chapter_name = read_page_controller.get_chapter_basic_infos_by_basic_object(o)[last_saw_index].name
        last_saw_index_label = QtWidgets.QLabel()
        # last_saw_index_label.setStyleSheet("font: 25 9pt \"等线 Light\";")
        last_saw_index_label.setText("🎞 " + last_saw_chapter_name)

        vertical_layout.addWidget(last_saw_index_label)

        vertical_layout.setSpacing(0)

        horizontal_layout.addLayout(vertical_layout)

        horizontal_layout.setSpacing(5)

        width = DisplayWidget(o)

        width.setLayout(horizontal_layout)

        return width

    def refresh_display_page_content(self):
        d = display_page_controller.get_novel_display_infos()

        if not d:
            # 没东西展示了
            self.display_table.clear()
            return

        row_cout = len(d)

        self.display_table.clear()
        self.display_table.setRowCount(row_cout)
        self.display_table.setColumnCount(1)

        width = self.display_table.width()

        row_height = self.display_table.height() * 0.3

        vertical_header = self.display_table.verticalHeader()

        vertical_header.setDefaultSectionSize(row_height)

        horizontal_header = self.display_table.horizontalHeader()

        horizontal_header.setDefaultSectionSize(width - 10)

        self.display_table.customContextMenuRequested.connect(self.generate_right_click_menu)

        i = 0
        for o in d.values():
            self.display_table.setCellWidget(i, 0, self.create_novel_display_width_by_object(o, width, row_height))

            i += 1

        logger.info("展示界面加载完毕")

        # 未改动前，此界面无需重复加载
        display_page_controller.display_page_is_loaded()

    def go_to_display_page(self) -> None:
        self.page.setCurrentIndex(1)

        logger.info("开始加载展示界面...")

        if not display_page_controller.is_display_page_need_to_reload_():
            logger.info("展示界面未变动，无需重新加载")
            return

        self.refresh_display_page_content()

    def tab_go_to_display_page(self, index):
        if index == 0:
            self.go_to_display_page()
        elif index == 3:
            self.setting_container.show()
            self.tab_pages.setCurrentIndex(1)

    def delete_novel_by_row_and_col(self, row, col):
        cell = self.display_table.cellWidget(row, col)

        if not cell:
            logger.warning("想删除不存在的cell")
            return

        novel_display_info = cell.novel_display_info

        id = novel_display_info.id

        logger.info("开始删除id为%d的小说..." % id)

        display_page_controller.delete_novel_by_id_from_cache(id)

        # 展示界面需要再加载
        display_page_controller.display_page_need_to_reload()
        # 直接再加载
        self.refresh_display_page_content()

        logger.info("删除完毕")

    def generate_right_click_menu(self, pos):
        row = col = -1
        # 获取选中的单元格的行数以及列数
        for i in self.display_table.selectionModel().selection().indexes():
            row = i.row()
            col = i.column()
        # 若选取的单元格中有元素，则支持右键菜单
        # if (row < self.crow) or (row == self.crow and col <= self.ccol):
        menu = QMenu()
        # 添加选项
        item2 = menu.addAction("删除")
        # 获取选项
        action = menu.exec_(self.display_table.mapToGlobal(pos))
        # 点击选项二，调用 self.delete_book 删除图书
        if action == item2:
            self.delete_novel_by_row_and_col(row, col)
            menu.close()
        else:
            menu.close()

    def add_a_novel_callback(self, flag: bool):
        if not flag:
            QMessageBox.information(self, "添加失败", "请输入合理的网址")
            return

        self.refresh_display_page_content()

    def add_a_novel(self):
        url, _ = QInputDialog.getText(self, "添加", "请输入网址:", QLineEdit.Normal, "")

        if not url:
            return

        self.t = AddThread(url)
        self.t.signal.connect(self.add_a_novel_callback)
        self.t.start()






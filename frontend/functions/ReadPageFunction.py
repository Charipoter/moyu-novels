import datetime

from PyQt5.QtCore import QStringListModel, QModelIndex
from PyQt5.QtWidgets import QMessageBox
from frontend.windows.MainWindow import MainWindow
from backend.controller.ReadPageController import read_page_controller
from backend.controller.DisplayPageController import display_page_controller
from backend.utils.LoggingConfiger import logger
from frontend.functions.threads.ContentThread import ContentThread


class ReadPageFunction(MainWindow):

    def refresh_content_by_object(self, o):
        self.content_container.clear()

        # 爬虫，并在爬完后更新界面
        self.t = ContentThread(o)
        self.t.signal.connect(self.set_content_by_object)
        self.t.start()

    def set_content_by_object(self, o):
        if not o:
            QMessageBox.information(self, "出错", "网络不太好")
            return

        # 标题
        self.content_container.append(o.title + "\n")

        for paragraph in o.paragraphs:
            self.content_container.append("　　" + paragraph + "\n")

        # 将滑轮位置改到顶端
        cursor = self.content_container.textCursor()

        cursor.setPosition(0)

        self.content_container.setTextCursor(cursor)

    def change_read_page(self, id: int, index: int):
        chapter_basic_info = read_page_controller.get_chapter_basic_info_by_id_and_index(id, index)

        if not chapter_basic_info:
            logger.error("章节索引出错")
            return

        # 如果索引没错，记录当前阅读信息进缓存
        read_page_controller.im_reading_the_id_and_index_of(id, index)

        # 本小说最后一次看的索引变化了，将缓存记录进内存数据库，必须在上面那句之下
        read_page_controller.put_last_saw_index_to_cache()

        self.refresh_content_by_object(chapter_basic_info)

        # 设置章节展示
        self.change_select_chapter_list_index(index)

        logger.info("阅读界面加载完毕")

    def init_read_page(self, row, col):
        logger.info("开始加载阅读界面...")

        display_cell = self.display_table.cellWidget(row, col)

        novel_display_info = display_cell.novel_display_info

        id = novel_display_info.id
        index = novel_display_info.last_saw_index
        last_update_time = novel_display_info.last_update_time

        # 设置tab页
        self.tab_pages.setCurrentIndex(1)

        if not read_page_controller.is_read_page_need_to_reload(id, index):
            logger.info("阅读界面未变动，无需加载")
            return

        # 时间不一样，展示界面得变化
        display_page_controller.display_page_need_to_reload()

        now = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")

        if last_update_time == "还没看过":
            read_page_controller.put_last_update_time_by_id_to_cache(id, now)
        else:
            if last_update_time < now:
                read_page_controller.put_last_update_time_by_id_to_cache(id, now)
            else:
                # 不满足，说明不用更新
                display_page_controller.display_page_is_loaded()

        # 如果变动了，记录当前阅读信息进缓存
        read_page_controller.im_reading_the_id_and_index_of(id, index)

        # 展示所有章节名
        self.select_chapter_list.clearSelection()

        chapter_basic_infos = read_page_controller.get_chapter_basic_infos_by_id(id)

        self.select_chapter_list_model = QStringListModel()

        self.select_chapter_list_model.setStringList([c.name for c in chapter_basic_infos])

        self.select_chapter_list.setModel(self.select_chapter_list_model)

        # 设置章节展示
        self.change_select_chapter_list_index(index)

        chapter_basic_info = chapter_basic_infos[index]

        self.refresh_content_by_object(chapter_basic_info)

        logger.info("阅读界面加载完毕")

    def go_to_read_page(self, row: int, col: int):
        self.page.setCurrentIndex(2)

        self.init_read_page(row, col)

    def go_to_another_page_by_index(self, index):
        id = read_page_controller.the_id_im_reading()

        # 展示界面得变化了
        display_page_controller.display_page_need_to_reload()

        self.change_read_page(id, index)

    def go_to_pre_chapter(self):
        logger.info("开始加载上一章阅读界面...")

        index = read_page_controller.the_index_im_reading() - 1

        self.go_to_another_page_by_index(index)

    def go_to_next_chapter(self):
        logger.info("开始加载下一章阅读界面...")

        index = read_page_controller.the_index_im_reading() + 1

        self.go_to_another_page_by_index(index)

    def go_to_select_chapter(self, index):
        logger.info("开始加载指定阅读界面...")

        self.tab_pages.setCurrentIndex(1)

        self.go_to_another_page_by_index(index.row())

    def change_select_chapter_list_index(self, index):
        i = self.select_chapter_list_model.index(index)
        self.select_chapter_list.setCurrentIndex(i)

    def close_setting_container(self):
        self.setting_container.close()


if __name__ == "__main__":
    now = datetime.datetime.now().strftime("%Y-%m-%d")

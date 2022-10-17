from frontend.windows.MainWindow import MainWindow
from config import resource_path
from frontend.functions.SettingFunction import SettingFunction


class StyleFunction(MainWindow):

    def __init__(self):
        super().__init__()

        self.content_container_style = {
            "QTextBrowser": {
                "font-size": "20px;",
                "line-height": "1.8;",
                "font-family": "'Microsoft YaHei',PingFangSC-Regular,HelveticaNeue-Light,'Helvetica Neue Light',"
                               "sans-serif;",

                "border": "",
                "color": "",
                "background-image": ""
            }

        }

        self.page_style = {
            "QWidget": {
                "background-image": ""
            },

            "QScrollBar:vertical": {
                "background": "transparent;",
                "width": "10px;",
                "margin": "0px 0px 0px 0px;"
            },
            "QScrollBar:vertical:hover": {
                "border-radius": "5px;",

                "background": "rgba(0, 0, 0, 0.06);"
            },
            "QScrollBar::handle:vertical": {
                "width": "10px;",
                "border-radius": "5px;",
                "border": "none;",

                "background": "rgba(0, 0, 0, 0.1);"
            },
            "QScrollBar::handle:vertical:hover": {
                "background": "rgba(0, 0, 0, 0.2);"
            },
            "QScrollBar::sub-line:vertical": {
                "height": "12px;",
                "width": "10px;",
                "background": "transparent;",
                "subcontrol-position": "top;"
            },
            "QScrollBar::add-line:vertical": {
                "height": "12px;",
                "width": "10px;",
                "background": "transparent;",
                "subcontrol-position": "bottom;"
            }
        }

        self.button_style = {
            "QPushButton": {
                "height": "25px;",
                "text-align": "center;",
                "font-size": "18px;",
                "font-family": "'Microsoft YaHei',PingFangSC-Regular,HelveticaNeue-Light,'Helvetica Neue Light',"
                               "sans-serif;",

                "color": "",
                "border": "",
                "background-image": "",
            },
            "QPushButton::hover": {
                "color": "",
                "background": ""
            }
        }

        self.display_table_style = {

            "font-size": "18px;",
            "border": "none;",
            "font-family": "'Microsoft YaHei',PingFangSC-Regular,HelveticaNeue-Light,'Helvetica Neue Light',"
                           "sans-serif;",


            "selection-background-color": "",
            "color": "",
            "background-image": ""

        }

        self.tab_pages_style = {
            "QTabWidget::pane": {
                "border": "none"
            },
            "QTabBar::tab": {
                "min-width": "15ex;",
                "min-height": "5ex;",
                "font-size": "18px;",
                "font-family": "'Microsoft YaHei',PingFangSC-Regular,HelveticaNeue-Light,'Helvetica Neue Light',"
                               "sans-serif;",
                "margin-left": "10px;",

                "border": "",
                "color": "",
                "background-image": "",
            },
            "QTabBar::tab:hover": {
                "color": "",
                "background": ""
            },
            "QTabBar::tab:selected": {
                "color": "",
                "background": ""
            }
        }

        self.select_chapter_list_style = {
            "QListView": {
                "font-size": "18px;",
                "line-height": "1.8;",

                "selection-background-color": "",
                "border": "",
                "color": "",
                "background-image": ""
            }
        }

        self.setting_container_style = {
            "font-size": "18px;",
            "font-family": "'Microsoft YaHei',PingFangSC-Regular,HelveticaNeue-Light,'Helvetica Neue Light',"
                           "sans-serif;",

            "color": "",
        }

        self.init_style()

    def init_style(self):
        self.theme0.setStyleSheet("background:url('%s');" % self.get_bg_path("basic_bg.png"))
        self.theme1.setStyleSheet("background:url('%s');" % self.get_bg_path("theme_1_bg.png"))
        self.theme2.setStyleSheet("background:url('%s');" % self.get_bg_path("theme_2_bg.png"))
        self.theme6.setStyleSheet("background:url('%s');" % self.get_bg_path("theme_6_bg.png"))

        theme = SettingFunction.get_theme()
        font = SettingFunction.get_font()
        font_size = SettingFunction.get_font_size()

        if theme == 0:
            self.set_default_style()
        elif theme == 1:
            self.set_theme1_style()
        elif theme == 2:
            self.set_theme2_style()
        else:
            self.set_theme6_style()

        if font == 0:
            self.set_font_style_to_yahei()
        elif font == 1:
            self.set_font_style_to_songti()
        else:
            self.set_font_style_to_kaiti()

        self.init_font_size(font_size)

    def set_content_container_style(self):
        s = ""
        for key, value in self.content_container_style.items():
            tmp = ""
            for k, v in value.items():
                tmp += "%s:%s" % (k, v)
            s += "%s{%s}" % (key, tmp)

        self.content_container.setStyleSheet(s)

    def set_page_style(self):
        s = ""
        for key, value in self.page_style.items():
            tmp = ""
            for k, v in value.items():
                tmp += "%s:%s" % (k, v)
            s += "%s{%s}" % (key, tmp)

        self.page.setStyleSheet(s)

    def set_button_style(self):
        s = ""
        for key, value in self.button_style.items():
            tmp = ""
            for k, v in value.items():
                tmp += "%s:%s" % (k, v)
            s += "%s{%s}" % (key, tmp)

        for button in [self.next_chapter_button, self.pre_chapter_button, self.add_button, self.start_button,
                       self.refresh_button, self.yahei, self.songti, self.kaiti, self.font_size_de, self.font_size_in,
                       self.close_setting_button]:
            button.setStyleSheet(s)

    def set_display_table_style(self):
        s = ""
        for key, value in self.display_table_style.items():
            s += "%s:%s" % (key, value)

        self.display_table.setStyleSheet(s)

    def set_tab_pages_style(self):
        s = ""
        for key, value in self.tab_pages_style.items():
            tmp = ""
            for k, v in value.items():
                tmp += "%s:%s" % (k, v)
            s += "%s{%s}" % (key, tmp)

        self.tab_pages.setStyleSheet(s)

    def set_select_chapter_list_style(self):
        s = ""
        for key, value in self.select_chapter_list_style.items():
            tmp = ""
            for k, v in value.items():
                tmp += "%s:%s" % (k, v)
            s += "%s{%s}" % (key, tmp)

        self.select_chapter_list.setStyleSheet(s)

    def set_setting_container_style(self):
        s = ""
        for key, value in self.setting_container_style.items():
            s += "%s:%s" % (key, value)

        self.setting_container.setStyleSheet(s)

    def get_bg_path(self, name) -> str:
        return (resource_path.BACKGROUND + name).replace("\\", "/")

    def set_content_container_color_style_to_default(self):
        bg_path = self.get_bg_path("basic_bg.png")
        self.content_container_style["QTextBrowser"]["background-image"] = "url(%s);" % bg_path
        self.content_container_style["QTextBrowser"]["border"] = "1px solid #d8d8d8;"
        self.content_container_style["QTextBrowser"]["color"] = "#262626;"

        self.set_content_container_style()

    def set_page_color_style_to_default(self):
        bg_path = self.get_bg_path("body_base_bg.png")
        self.page_style["QWidget"]["background-image"] = "url(%s);" % bg_path

        self.page_style["QScrollBar:vertical:hover"]["background"] = "rgba(0, 0, 0, 0.06);"
        self.page_style["QScrollBar::handle:vertical"]["background"] = "rgba(0, 0, 0, 0.1);"
        self.page_style["QScrollBar::handle:vertical:hover"]["background"] = "rgba(0, 0, 0, 0.2);"

        self.set_page_style()

    def set_button_color_style_to_default(self):
        bg_path = self.get_bg_path("basic_bg.png")
        self.button_style["QPushButton"]["background-image"] = "url(%s);" % bg_path
        self.button_style["QPushButton"]["border"] = "1px solid #d8d8d8;"
        self.button_style["QPushButton"]["color"] = "#262626;"

        self.button_style["QPushButton::hover"]["color"] = "#262626;"
        self.button_style["QPushButton::hover"]["background"] = "rgba(0,0,0,.03);"

        self.set_button_style()

    def set_display_table_style_to_default(self):
        bg_path = self.get_bg_path("basic_bg.png")
        self.display_table_style["background-image"] = "url(%s);" % bg_path
        self.display_table_style["color"] = "#262626;"
        self.display_table_style["selection-background-color"] = "rgba(0,0,0,.03);"

        self.set_display_table_style()

    def set_tab_pages_style_to_default(self):
        bg_path = self.get_bg_path("basic_bg.png")
        self.tab_pages_style["QTabBar::tab"]["background-image"] = "url(%s);" % bg_path
        self.tab_pages_style["QTabBar::tab"]["color"] = "#262626;"
        self.tab_pages_style["QTabBar::tab"]["border"] = "1px solid #d8d8d8;"

        self.tab_pages_style["QTabBar::tab:hover"]["background"] = "rgba(0,0,0,.03);"
        self.tab_pages_style["QTabBar::tab:hover"]["color"] = "#262626;"

        self.tab_pages_style["QTabBar::tab:selected"]["background"] = "rgba(0,0,0,.03);"
        self.tab_pages_style["QTabBar::tab:selected"]["color"] = "#262626;"

        self.set_tab_pages_style()

    def set_select_chapter_list_style_to_default(self):
        bg_path = self.get_bg_path("basic_bg.png")
        self.select_chapter_list_style["QListView"]["background-image"] = "url(%s);" % bg_path
        self.select_chapter_list_style["QListView"]["border"] = "1px solid #d8d8d8;"
        self.select_chapter_list_style["QListView"]["color"] = "#262626;"
        self.select_chapter_list_style["QListView"]["selection-background-color"] = "rgba(0,0,0,.03);"

        self.set_select_chapter_list_style()

    def set_setting_container_style_to_default(self):
        self.setting_container_style["color"] = "#262626;"

        self.set_setting_container_style()

    def set_default_style(self):
        self.set_page_color_style_to_default()
        self.set_content_container_color_style_to_default()
        self.set_button_color_style_to_default()
        self.set_display_table_style_to_default()
        self.set_tab_pages_style_to_default()
        self.set_select_chapter_list_style_to_default()
        self.set_setting_container_style_to_default()
        SettingFunction.change_theme(0)

    def set_content_container_color_style_to_theme1(self):
        bg_path = self.get_bg_path("theme_1_bg.png")
        self.content_container_style["QTextBrowser"]["background-image"] = "url(%s);" % bg_path
        self.content_container_style["QTextBrowser"]["border"] = "1px solid #d8d8d8;"
        self.content_container_style["QTextBrowser"]["color"] = "#262626;"

        self.set_content_container_style()

    def set_page_color_style_to_theme1(self):
        bg_path = self.get_bg_path("body_theme1_bg.png")
        self.page_style["QWidget"]["background-image"] = "url(%s);" % bg_path

        self.page_style["QScrollBar:vertical:hover"]["background"] = "rgba(0, 0, 0, 0.06);"
        self.page_style["QScrollBar::handle:vertical"]["background"] = "rgba(0, 0, 0, 0.1);"
        self.page_style["QScrollBar::handle:vertical:hover"]["background"] = "rgba(0, 0, 0, 0.2);"

        self.set_page_style()

    def set_button_color_style_to_theme1(self):
        bg_path = self.get_bg_path("theme_1_bg.png")
        self.button_style["QPushButton"]["background-image"] = "url(%s);" % bg_path
        self.button_style["QPushButton"]["border"] = "1px solid #d8d8d8;"
        self.button_style["QPushButton"]["color"] = "#262626;"

        self.button_style["QPushButton::hover"]["color"] = "#262626;"
        self.button_style["QPushButton::hover"]["background"] = "rgba(0,0,0,.03);"

        self.set_button_style()

    def set_display_table_style_to_theme1(self):
        bg_path = self.get_bg_path("theme_1_bg.png")
        self.display_table_style["background-image"] = "url(%s);" % bg_path
        self.display_table_style["color"] = "#262626;"
        self.display_table_style["selection-background-color"] = "rgba(0,0,0,.03);"

        self.set_display_table_style()

    def set_tab_pages_style_to_theme1(self):
        bg_path = self.get_bg_path("theme_1_bg.png")
        self.tab_pages_style["QTabBar::tab"]["background-image"] = "url(%s);" % bg_path
        self.tab_pages_style["QTabBar::tab"]["color"] = "#262626;"
        self.tab_pages_style["QTabBar::tab"]["border"] = "1px solid #d8d8d8;"

        self.tab_pages_style["QTabBar::tab:hover"]["background"] = "rgba(0,0,0,.03);"
        self.tab_pages_style["QTabBar::tab:hover"]["color"] = "#262626;"

        self.tab_pages_style["QTabBar::tab:selected"]["background"] = "rgba(0,0,0,.03);"
        self.tab_pages_style["QTabBar::tab:selected"]["color"] = "#262626;"

        self.set_tab_pages_style()

    def set_select_chapter_list_style_to_theme1(self):
        bg_path = self.get_bg_path("theme_1_bg.png")
        self.select_chapter_list_style["QListView"]["background-image"] = "url(%s);" % bg_path
        self.select_chapter_list_style["QListView"]["border"] = "1px solid #d8d8d8;"
        self.select_chapter_list_style["QListView"]["color"] = "#262626;"
        self.select_chapter_list_style["QListView"]["selection-background-color"] = "rgba(0,0,0,.03);"

        self.set_select_chapter_list_style()

    def set_setting_container_style_to_theme1(self):
        self.setting_container_style["color"] = "#262626;"

        self.set_setting_container_style()

    def set_theme1_style(self):
        self.set_page_color_style_to_theme1()
        self.set_content_container_color_style_to_theme1()
        self.set_button_color_style_to_theme1()
        self.set_display_table_style_to_theme1()
        self.set_tab_pages_style_to_theme1()
        self.set_select_chapter_list_style_to_theme1()
        self.set_setting_container_style_to_theme1()
        SettingFunction.change_theme(1)

    def set_content_container_color_style_to_theme2(self):
        bg_path = self.get_bg_path("theme_2_bg.png")
        self.content_container_style["QTextBrowser"]["background-image"] = "url(%s);" % bg_path
        self.content_container_style["QTextBrowser"]["border"] = "1px solid #d8d8d8;"
        self.content_container_style["QTextBrowser"]["color"] = "#262626;"

        self.set_content_container_style()

    def set_page_color_style_to_theme2(self):
        bg_path = self.get_bg_path("body_theme2_bg.png")
        self.page_style["QWidget"]["background-image"] = "url(%s);" % bg_path

        self.page_style["QScrollBar:vertical:hover"]["background"] = "rgba(0, 0, 0, 0.06);"
        self.page_style["QScrollBar::handle:vertical"]["background"] = "rgba(0, 0, 0, 0.1);"
        self.page_style["QScrollBar::handle:vertical:hover"]["background"] = "rgba(0, 0, 0, 0.2);"

        self.set_page_style()

    def set_button_color_style_to_theme2(self):
        bg_path = self.get_bg_path("theme_2_bg.png")
        self.button_style["QPushButton"]["background-image"] = "url(%s);" % bg_path
        self.button_style["QPushButton"]["border"] = "1px solid #d8d8d8;"
        self.button_style["QPushButton"]["color"] = "#262626;"

        self.button_style["QPushButton::hover"]["color"] = "#262626;"
        self.button_style["QPushButton::hover"]["background"] = "rgba(0,0,0,.03);"

        self.set_button_style()

    def set_display_table_style_to_theme2(self):
        bg_path = self.get_bg_path("theme_2_bg.png")
        self.display_table_style["background-image"] = "url(%s);" % bg_path
        self.display_table_style["color"] = "#262626;"
        self.display_table_style["selection-background-color"] = "rgba(0,0,0,.03);"

        self.set_display_table_style()

    def set_tab_pages_style_to_theme2(self):
        bg_path = self.get_bg_path("theme_2_bg.png")
        self.tab_pages_style["QTabBar::tab"]["background-image"] = "url(%s);" % bg_path
        self.tab_pages_style["QTabBar::tab"]["color"] = "#262626;"
        self.tab_pages_style["QTabBar::tab"]["border"] = "1px solid #d8d8d8;"

        self.tab_pages_style["QTabBar::tab:hover"]["background"] = "rgba(0,0,0,.03);"
        self.tab_pages_style["QTabBar::tab:hover"]["color"] = "#262626;"

        self.tab_pages_style["QTabBar::tab:selected"]["background"] = "rgba(0,0,0,.03);"
        self.tab_pages_style["QTabBar::tab:selected"]["color"] = "#262626;"

        self.set_tab_pages_style()

    def set_select_chapter_list_style_to_theme2(self):
        bg_path = self.get_bg_path("theme_2_bg.png")
        self.select_chapter_list_style["QListView"]["background-image"] = "url(%s);" % bg_path
        self.select_chapter_list_style["QListView"]["border"] = "1px solid #d8d8d8;"
        self.select_chapter_list_style["QListView"]["color"] = "#262626;"
        self.select_chapter_list_style["QListView"]["selection-background-color"] = "rgba(0,0,0,.03);"

        self.set_select_chapter_list_style()

    def set_setting_container_style_to_theme2(self):
        self.setting_container_style["color"] = "#262626;"

        self.set_setting_container_style()

    def set_theme2_style(self):
        self.set_page_color_style_to_theme2()
        self.set_content_container_color_style_to_theme2()
        self.set_button_color_style_to_theme2()
        self.set_display_table_style_to_theme2()
        self.set_tab_pages_style_to_theme2()
        self.set_select_chapter_list_style_to_theme2()
        self.set_setting_container_style_to_theme2()
        SettingFunction.change_theme(2)

    def set_content_container_color_style_to_theme6(self):
        bg_path = self.get_bg_path("theme_6_bg.png")
        self.content_container_style["QTextBrowser"]["background-image"] = "url(%s);" % bg_path
        self.content_container_style["QTextBrowser"]["color"] = "#666;"
        self.content_container_style["QTextBrowser"]["border"] = "1px solid #444;"

        self.set_content_container_style()

    def set_page_color_style_to_theme6(self):
        bg_path = self.get_bg_path("body_theme6_bg.png")
        self.page_style["QWidget"]["background-image"] = "url(%s);" % bg_path

        self.page_style["QScrollBar:vertical:hover"]["background"] = "rgba(255, 255, 255, 0.06);"
        self.page_style["QScrollBar::handle:vertical"]["background"] = "rgba(255, 255, 255, 0.1);"
        self.page_style["QScrollBar::handle:vertical:hover"]["background"] = "rgba(255, 255, 255, 0.2);"

        self.set_page_style()

    def set_button_color_style_to_theme6(self):
        bg_path = self.get_bg_path("theme_6_bg.png")
        self.button_style["QPushButton"]["background-image"] = "url(%s);" % bg_path
        self.button_style["QPushButton"]["border"] = "1px solid #444;"
        self.button_style["QPushButton"]["color"] = "#666;"

        self.button_style["QPushButton::hover"]["color"] = "#ed4259;"
        self.button_style["QPushButton::hover"]["background"] = "rgba(255,255,255,.1);"

        self.set_button_style()

    def set_display_table_style_to_theme6(self):
        bg_path = self.get_bg_path("theme_6_bg.png")
        self.display_table_style["background-image"] = "url(%s);" % bg_path
        self.display_table_style["color"] = "#666;"
        self.display_table_style["selection-background-color"] = "rgba(255,255,255,.1);"

        self.set_display_table_style()

    def set_tab_pages_style_to_theme6(self):
        bg_path = self.get_bg_path("theme_6_bg.png")
        self.tab_pages_style["QTabBar::tab"]["background-image"] = "url(%s);" % bg_path
        self.tab_pages_style["QTabBar::tab"]["color"] = "#666;"
        self.tab_pages_style["QTabBar::tab"]["border"] = "1px solid #444;"

        self.tab_pages_style["QTabBar::tab:hover"]["background"] = "rgba(255,255,255,.1);"
        self.tab_pages_style["QTabBar::tab:hover"]["color"] = "#ed4259;"

        self.tab_pages_style["QTabBar::tab:selected"]["background"] = "rgba(255,255,255,.1);"
        self.tab_pages_style["QTabBar::tab:selected"]["color"] = "#666;"

        self.set_tab_pages_style()

    def set_select_chapter_list_style_to_theme6(self):
        bg_path = self.get_bg_path("theme_6_bg.png")
        self.select_chapter_list_style["QListView"]["background-image"] = "url(%s);" % bg_path
        self.select_chapter_list_style["QListView"]["border"] = "1px solid #444;"
        self.select_chapter_list_style["QListView"]["color"] = "#666;"
        self.select_chapter_list_style["QListView"]["selection-background-color"] = "rgba(255,255,255,.1);"

        self.set_select_chapter_list_style()

    def set_setting_container_style_to_theme6(self):
        self.setting_container_style["color"] = "#666;"

        self.set_setting_container_style()

    def set_theme6_style(self):
        self.set_page_color_style_to_theme6()
        self.set_content_container_color_style_to_theme6()
        self.set_button_color_style_to_theme6()
        self.set_display_table_style_to_theme6()
        self.set_tab_pages_style_to_theme6()
        self.set_select_chapter_list_style_to_theme6()
        self.set_setting_container_style_to_theme6()
        SettingFunction.change_theme(6)

    def set_font_style_to_yahei(self):
        self.content_container_style["QTextBrowser"]["font-family"] = "'Microsoft YaHei',PingFangSC-Regular," \
                                                                      "HelveticaNeue-Light,'Helvetica Neue Light'," \
                                                                      "sans-serif;"

        self.set_content_container_style()
        SettingFunction.change_font(0)

    def set_font_style_to_songti(self):
        self.content_container_style["QTextBrowser"]["font-family"] = "PingFangSC-Regular,'-apple-system',Simsun;"

        self.set_content_container_style()
        SettingFunction.change_font(1)

    def set_font_style_to_kaiti(self):
        self.content_container_style["QTextBrowser"]["font-family"] = "Kaiti;"

        self.set_content_container_style()
        SettingFunction.change_font(2)

    def increase_font_size(self):
        size = SettingFunction.get_font_size() + 1
        self.content_container_style["QTextBrowser"]["font-size"] = "%dpx;" % size

        self.font_size_label.setText(str(size))

        self.set_content_container_style()
        SettingFunction.change_font_size(size)

    def decrease_font_size(self):
        size = SettingFunction.get_font_size() - 1
        self.content_container_style["QTextBrowser"]["font-size"] = "%dpx;" % size

        self.font_size_label.setText(str(size))

        self.set_content_container_style()
        SettingFunction.change_font_size(size)

    def init_font_size(self, size):
        self.content_container_style["QTextBrowser"]["font-size"] = "%dpx;" % size

        self.font_size_label.setText(str(size))

        self.set_content_container_style()


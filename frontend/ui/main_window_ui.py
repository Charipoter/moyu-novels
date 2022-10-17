# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(664, 869)
        Form.setStyleSheet("")
        self.gridLayout_10 = QtWidgets.QGridLayout(Form)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.page = QtWidgets.QStackedWidget(Form)
        self.page.setStyleSheet("")
        self.page.setObjectName("page")
        self.start_page = QtWidgets.QWidget()
        self.start_page.setObjectName("start_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.start_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.start_button = QtWidgets.QPushButton(self.start_page)
        self.start_button.setStyleSheet("")
        self.start_button.setObjectName("start_button")
        self.gridLayout_2.addWidget(self.start_button, 0, 0, 1, 1)
        self.page.addWidget(self.start_page)
        self.display_page = QtWidgets.QWidget()
        self.display_page.setObjectName("display_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.display_page)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.display_table = MyTableWidget(self.display_page)
        self.display_table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.display_table.setStyleSheet("")
        self.display_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.display_table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.display_table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.display_table.setShowGrid(False)
        self.display_table.setObjectName("display_table")
        self.display_table.setColumnCount(0)
        self.display_table.setRowCount(0)
        self.display_table.horizontalHeader().setVisible(False)
        self.display_table.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.display_table, 4, 1, 1, 2)
        self.refresh_button = QtWidgets.QPushButton(self.display_page)
        self.refresh_button.setStyleSheet("")
        self.refresh_button.setObjectName("refresh_button")
        self.gridLayout.addWidget(self.refresh_button, 1, 1, 1, 1)
        self.add_button = QtWidgets.QPushButton(self.display_page)
        self.add_button.setStyleSheet("")
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 1, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.page.addWidget(self.display_page)
        self.read_page = QtWidgets.QWidget()
        self.read_page.setStyleSheet("")
        self.read_page.setObjectName("read_page")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.read_page)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tab_pages = QtWidgets.QTabWidget(self.read_page)
        self.tab_pages.setStyleSheet("")
        self.tab_pages.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab_pages.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_pages.setDocumentMode(False)
        self.tab_pages.setTabsClosable(False)
        self.tab_pages.setTabBarAutoHide(False)
        self.tab_pages.setObjectName("tab_pages")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tab_pages.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 5, 10, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.content_container = QtWidgets.QTextBrowser(self.tab)
        self.content_container.setStyleSheet("")
        self.content_container.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.content_container.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.content_container.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.content_container.setLineWrapColumnOrWidth(0)
        self.content_container.setObjectName("content_container")
        self.verticalLayout.addWidget(self.content_container)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, 0, 10)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pre_chapter_button = QtWidgets.QPushButton(self.tab)
        self.pre_chapter_button.setStyleSheet("")
        self.pre_chapter_button.setObjectName("pre_chapter_button")
        self.horizontalLayout.addWidget(self.pre_chapter_button)
        self.next_chapter_button = QtWidgets.QPushButton(self.tab)
        self.next_chapter_button.setStyleSheet("")
        self.next_chapter_button.setObjectName("next_chapter_button")
        self.horizontalLayout.addWidget(self.next_chapter_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.setting_container = QtWidgets.QDockWidget(self.tab)
        self.setting_container.setAcceptDrops(True)
        self.setting_container.setAutoFillBackground(False)
        self.setting_container.setFloating(False)
        self.setting_container.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.setting_container.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.setting_container.setObjectName("setting_container")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.close_setting_button = QtWidgets.QPushButton(self.dockWidgetContents)
        self.close_setting_button.setObjectName("close_setting_button")
        self.gridLayout_4.addWidget(self.close_setting_button, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.theme0 = QtWidgets.QPushButton(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.theme0.sizePolicy().hasHeightForWidth())
        self.theme0.setSizePolicy(sizePolicy)
        self.theme0.setMaximumSize(QtCore.QSize(28, 16777215))
        self.theme0.setStyleSheet("")
        self.theme0.setText("")
        self.theme0.setObjectName("theme0")
        self.horizontalLayout_2.addWidget(self.theme0)
        self.theme1 = QtWidgets.QPushButton(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.theme1.sizePolicy().hasHeightForWidth())
        self.theme1.setSizePolicy(sizePolicy)
        self.theme1.setMaximumSize(QtCore.QSize(28, 16777215))
        self.theme1.setStyleSheet("")
        self.theme1.setText("")
        self.theme1.setObjectName("theme1")
        self.horizontalLayout_2.addWidget(self.theme1)
        self.theme2 = QtWidgets.QPushButton(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.theme2.sizePolicy().hasHeightForWidth())
        self.theme2.setSizePolicy(sizePolicy)
        self.theme2.setMaximumSize(QtCore.QSize(28, 16777215))
        self.theme2.setStyleSheet("")
        self.theme2.setText("")
        self.theme2.setObjectName("theme2")
        self.horizontalLayout_2.addWidget(self.theme2)
        self.theme6 = QtWidgets.QPushButton(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.theme6.sizePolicy().hasHeightForWidth())
        self.theme6.setSizePolicy(sizePolicy)
        self.theme6.setMaximumSize(QtCore.QSize(28, 16777215))
        self.theme6.setStyleSheet("")
        self.theme6.setText("")
        self.theme6.setObjectName("theme6")
        self.horizontalLayout_2.addWidget(self.theme6)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.yahei = QtWidgets.QPushButton(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yahei.sizePolicy().hasHeightForWidth())
        self.yahei.setSizePolicy(sizePolicy)
        self.yahei.setMaximumSize(QtCore.QSize(50, 16777215))
        self.yahei.setObjectName("yahei")
        self.horizontalLayout_3.addWidget(self.yahei)
        self.songti = QtWidgets.QPushButton(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songti.sizePolicy().hasHeightForWidth())
        self.songti.setSizePolicy(sizePolicy)
        self.songti.setMaximumSize(QtCore.QSize(50, 16777215))
        self.songti.setObjectName("songti")
        self.horizontalLayout_3.addWidget(self.songti)
        self.kaiti = QtWidgets.QPushButton(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kaiti.sizePolicy().hasHeightForWidth())
        self.kaiti.setSizePolicy(sizePolicy)
        self.kaiti.setMaximumSize(QtCore.QSize(50, 16777215))
        self.kaiti.setObjectName("kaiti")
        self.horizontalLayout_3.addWidget(self.kaiti)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.font_size_de = QtWidgets.QPushButton(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.font_size_de.sizePolicy().hasHeightForWidth())
        self.font_size_de.setSizePolicy(sizePolicy)
        self.font_size_de.setMaximumSize(QtCore.QSize(50, 16777215))
        self.font_size_de.setObjectName("font_size_de")
        self.horizontalLayout_4.addWidget(self.font_size_de)
        self.font_size_label = QtWidgets.QLabel(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.font_size_label.sizePolicy().hasHeightForWidth())
        self.font_size_label.setSizePolicy(sizePolicy)
        self.font_size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.font_size_label.setObjectName("font_size_label")
        self.horizontalLayout_4.addWidget(self.font_size_label)
        self.font_size_in = QtWidgets.QPushButton(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.font_size_in.sizePolicy().hasHeightForWidth())
        self.font_size_in.setSizePolicy(sizePolicy)
        self.font_size_in.setMaximumSize(QtCore.QSize(50, 16777215))
        self.font_size_in.setObjectName("font_size_in")
        self.horizontalLayout_4.addWidget(self.font_size_in)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)
        self.gridLayout_4.setColumnStretch(1, 5)
        self.setting_container.setWidget(self.dockWidgetContents)
        self.verticalLayout.addWidget(self.setting_container)
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tab_pages.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.select_chapter_list = QtWidgets.QListView(self.tab_2)
        self.select_chapter_list.setStyleSheet("")
        self.select_chapter_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.select_chapter_list.setObjectName("select_chapter_list")
        self.gridLayout_7.addWidget(self.select_chapter_list, 0, 0, 1, 1)
        self.tab_pages.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tab_pages.addTab(self.tab_4, "")
        self.gridLayout_6.addWidget(self.tab_pages, 0, 0, 1, 1)
        self.page.addWidget(self.read_page)
        self.gridLayout_10.addWidget(self.page, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.page.setCurrentIndex(0)
        self.tab_pages.setCurrentIndex(1)
        self.start_button.clicked.connect(Form.go_to_display_page)
        self.display_table.cellDoubleClicked['int','int'].connect(Form.go_to_read_page)
        self.pre_chapter_button.clicked.connect(Form.go_to_pre_chapter)
        self.next_chapter_button.clicked.connect(Form.go_to_next_chapter)
        self.add_button.clicked.connect(Form.add_a_novel)
        self.refresh_button.clicked.connect(Form.refresh_display_page_content)
        self.select_chapter_list.doubleClicked['QModelIndex'].connect(Form.go_to_select_chapter)
        self.tab_pages.currentChanged['int'].connect(Form.tab_go_to_display_page)
        self.theme0.clicked.connect(Form.set_default_style)
        self.theme1.clicked.connect(Form.set_theme1_style)
        self.theme2.clicked.connect(Form.set_theme2_style)
        self.theme6.clicked.connect(Form.set_theme6_style)
        self.yahei.clicked.connect(Form.set_font_style_to_yahei)
        self.songti.clicked.connect(Form.set_font_style_to_songti)
        self.kaiti.clicked.connect(Form.set_font_style_to_kaiti)
        self.font_size_de.clicked.connect(Form.decrease_font_size)
        self.font_size_in.clicked.connect(Form.increase_font_size)
        self.close_setting_button.clicked.connect(Form.close_setting_container)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.start_button.setText(_translate("Form", "开始阅读"))
        self.refresh_button.setText(_translate("Form", "手动刷新"))
        self.add_button.setText(_translate("Form", "添加小说"))
        self.tab_pages.setTabText(self.tab_pages.indexOf(self.tab_3), _translate("Form", "返回"))
        self.content_container.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pre_chapter_button.setText(_translate("Form", "上一章"))
        self.next_chapter_button.setText(_translate("Form", "下一章"))
        self.close_setting_button.setText(_translate("Form", "关闭"))
        self.label.setText(_translate("Form", "阅读主题"))
        self.label_2.setText(_translate("Form", "正文字体"))
        self.yahei.setText(_translate("Form", "雅黑"))
        self.songti.setText(_translate("Form", "宋体"))
        self.kaiti.setText(_translate("Form", "楷体"))
        self.label_3.setText(_translate("Form", "字体大小"))
        self.font_size_de.setText(_translate("Form", "A-"))
        self.font_size_label.setText(_translate("Form", "20"))
        self.font_size_in.setText(_translate("Form", "A+"))
        self.tab_pages.setTabText(self.tab_pages.indexOf(self.tab), _translate("Form", "阅读"))
        self.tab_pages.setTabText(self.tab_pages.indexOf(self.tab_2), _translate("Form", "章节"))
        self.tab_pages.setTabText(self.tab_pages.indexOf(self.tab_4), _translate("Form", "设置"))
from frontend.functions.MyTableWidget import MyTableWidget

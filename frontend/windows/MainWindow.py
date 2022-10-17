from PyQt5.QtWidgets import QWidget

from frontend.ui.main_window_ui import Ui_Form


class MainWindow(Ui_Form, QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
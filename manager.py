import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen, QStyleFactory

from frontend.MainFunction import MainFunction
import config


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))

    splash = QSplashScreen(QPixmap("resource\\splash\\splash.png"))  # 启动界面图片地址
    splash.show()

    app.processEvents()
    window = MainFunction()
    window.show()

    splash.finish(window)

    sys.exit(app.exec_())
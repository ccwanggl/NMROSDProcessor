from PyQt6.QtCore import QRect, QSize
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt6 import QtGui
import sys


def ClickMe():
    sys.exit()


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        title = "PyQt6 Push Button"
        left = 500
        top = 200
        width = 300
        height = 250
        iconName = "home.png"

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, top, width, height)

    def UiComponents(self):
        button = QPushButton("Close Window", self)
        button.setGeometry(QRect(100, 100, 111, 50))
        button.setIcon(QtGui.QIcon("home.png"))
        button.setIconSize(QSize(40,40))
        button.setToolTip("This Is Click Me Button")
        button.clicked.connect(ClickMe)

    def ClickMe(self):
        sys.exit()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.UiComponents()

    window.show()
    sys.exit(App.exec())

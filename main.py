# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtGui
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt6 Window"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()

    sys.exit(App.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

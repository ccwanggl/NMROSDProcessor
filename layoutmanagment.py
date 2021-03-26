import sys

from PyQt6 import QtGui
from PyQt6.QtCore import QRect, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton


class Window(QDialog):
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

        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()

    def createLayout(self):
        self.groupBox = QGroupBox("What Is Your Favorite Sport?")

        hboxlayout = QHBoxLayout()

        self.button = QPushButton("Football", self)
        self.button.setIcon(QtGui.QIcon("home.png"))
        self.button.setIconSize(QSize(40, 40))
        self.button.setToolTip("This Is Click Me Button")
        self.button.setMinimumHeight(40)
        hboxlayout.addWidget(self.button)

        self.button1 = QPushButton("Cricket", self)
        self.button1.setIcon(QtGui.QIcon("home.png"))
        self.button1.setIconSize(QSize(40, 40))
        self.button1.setMinimumHeight(40)
        self.button1.setToolTip("This Is Click Me Button")
        hboxlayout.addWidget(self.button1)

        self.button2 = QPushButton("Tennis", self)
        self.button2.setIcon(QtGui.QIcon("home.png"))
        self.button2.setIconSize(QSize(40, 40))
        self.button2.setMinimumHeight(40)
        self.button2.setToolTip("This Is Click Me Button")
        hboxlayout.addWidget(self.button2)

        self.groupBox.setLayout(hboxlayout)

# Press the green 1button in the gutter 1to run the script.
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()

    sys.exit(App.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import sys

from PyQt6 import QtGui
from PyQt6.QtCore import QRect, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout



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
        self.groupBox = QGroupBox("What is your favorite programming language?")

        gridLayout = QGridLayout()

        button1 = QPushButton("Python", self)
        gridLayout.addWidget(button1, 0, 0)


        button2 = QPushButton("C++", self)
        gridLayout.addWidget(button2, 0, 1)


        button3 = QPushButton("Java", self)
        gridLayout.addWidget(button3, 1, 0)


        button4 = QPushButton("C#", self)
        gridLayout.addWidget(button4, 1, 1)

        self.groupBox.setLayout(gridLayout)

# Press the green 1button in the gutter 1to run the script.
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()

    sys.exit(App.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

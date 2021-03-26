import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QDialog, QVBoxLayout
from PyQt6 import QtGui


class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()

        self.title = "PyQt6 Window"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "home.png"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        label = QLabel("This is PyQt6 Label")
        vbox.addWidget(label)

        label2 = QLabel("This is PyQt6 GUI Application Development")
        label2.setFont(QtGui.QFont("Sanserif ", 20))
        label2.setStyleSheet('color:red')
        vbox.addWidget(label2)

        self.setLayout(vbox)

        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

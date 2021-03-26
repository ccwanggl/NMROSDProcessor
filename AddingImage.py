import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QDialog, QVBoxLayout
from PyQt6 import QtGui
from PyQt6.QtGui import QPixmap


class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()

        self.title = "PyQt6 Window"
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 300
        self.iconName = "home.png"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("resources/pyqt5_image_window-300x180.png")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)

        self.setLayout(vbox)

        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

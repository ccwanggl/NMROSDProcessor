import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QRadioButton, QVBoxLayout, QGroupBox, QCheckBox, \
    QHBoxLayout, QLineEdit
from PyQt6.QtGui import QIcon, QFont


class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()

        self.groupBox = QGroupBox("What is your favorite programming Language ?")
        self.groupBox.setFont(QFont("Sanserif", 13))

        self.lineEdit = QLineEdit()

        self.label = QLabel("You input string is :")
        self.title = " "
        self.left = 100
        self.top = 200
        self.width = 400
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createLineEdit()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

        self.show()

    def createLineEdit(self):
        hboxLayout = QHBoxLayout()

        self.lineEdit.returnPressed.connect(self.onReturn_pressed)
        hboxLayout.addWidget(self.lineEdit)


        self.groupBox.setLayout(hboxLayout)

    def onReturn_pressed(self):
        self.label.setText(self.lineEdit.text())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()

    sys.exit(App.exec())

import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QRadioButton, QVBoxLayout, QGroupBox, \
    QHBoxLayout
from PyQt6.QtGui import QIcon


class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()

        self.groupBox = QGroupBox("What is your favorite sport ?")
        self.radiobtn3 = QRadioButton("BasketBall")
        self.radiobtn3.setIcon(QIcon(""))
        self.radiobtn2 = QRadioButton("Swimming")
        self.radiobtn2.setIcon(QIcon(""))
        self.radiobtn1 = QRadioButton("FootBall")
        self.radiobtn1.setIcon(QIcon(""))

        self.label = QLabel("You Have Selected FootBall")
        self.title = " "
        self.left = 100
        self.top = 200
        self.width = 400
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.radioButton()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

        self.show()

    def radioButton(self):
        hbox = QHBoxLayout()

        self.radiobtn1.setChecked(True)
        self.radiobtn1.toggled.connect(self.OnRadioButton)
        hbox.addWidget(self.radiobtn1)

        self.radiobtn2.setChecked(False)
        self.radiobtn2.toggled.connect(self.OnRadioButton)
        hbox.addWidget(self.radiobtn2)

        self.radiobtn3.setChecked(False)
        self.radiobtn2.toggled.connect(self.OnRadioButton)
        hbox.addWidget(self.radiobtn3)

        self.groupBox.setLayout(hbox)

    def OnRadioButton(self):
        # Which radioBtn send message
        radioBtn = self.sender()

        if radioBtn.isChecked():
            self.label.setText("You Have Selected " + radioBtn.text())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()

    sys.exit(App.exec())

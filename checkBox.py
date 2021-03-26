import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QRadioButton, QVBoxLayout, QGroupBox, QCheckBox, \
    QHBoxLayout
from PyQt6.QtGui import QIcon, QFont


class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()

        self.groupBox = QGroupBox("What is your favorite programming Language ?")
        self.groupBox.setFont(QFont("Sanserif", 13))

        self.checkBox1 = QCheckBox("Python")
        self.checkBox1.setIcon(QIcon(""))
        self.checkBox1.setWhatsThis("This is a checkbox of Python")

        self.checkBox2 = QCheckBox("C++")
        self.checkBox2.setIcon(QIcon(""))
        self.checkBox1.setWhatsThis("This is a checkbox of C++")

        self.checkBox3 = QCheckBox("Java")
        self.checkBox3.setIcon(QIcon(""))
        self.checkBox1.setWhatsThis("This is a checkbox of Java")

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

        self.createCheckBox()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

        self.show()

    def createCheckBox(self):
        hboxLayout = QHBoxLayout()

        self.checkBox1.toggled.connect(self.onCheckBox_Toggled)
        hboxLayout.addWidget(self.checkBox1)

        self.checkBox2.toggled.connect(self.onCheckBox_Toggled)
        hboxLayout.addWidget(self.checkBox2)

        self.checkBox3.toggled.connect(self.onCheckBox_Toggled)
        hboxLayout.addWidget(self.checkBox3)

        self.groupBox.setLayout(hboxLayout)

    def onCheckBox_Toggled(self):
        if self.checkBox1.isChecked():
            self.label.setText("You Have Select : " + self.checkBox1.text())

        if self.checkBox2.isChecked():
            self.label.setText("You Have Select : " + self.checkBox2.text())

        if self.checkBox3.isChecked():
            self.label.setText("You Have Select : " + self.checkBox3.text())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()

    sys.exit(App.exec())

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
import sys

class Widget1(QWidget):
    def __init__(self, btnname):
        super().__init__()
        self.lay = QVBoxLayout()
        self.btn1 = QPushButton(btnname + "1")
        self.setLayout(self.lay)
        self.lay.addWidget(self.btn1)

class Widget2(QWidget):
    def __init__(self, btnname):
        super().__init__()
        self.lay = QVBoxLayout()
        self.btn1 = QPushButton(btnname + "1")
        self.btn2 = QPushButton(btnname + "2")
        self.setLayout(self.lay)
        self.lay.addWidget(self.btn1)
        self.lay.addWidget(self.btn2)

class Widget3(QWidget):
    def __init__(self, btnname):
        super().__init__()
        self.lay = QVBoxLayout()
        self.btn1 = QPushButton(btnname + "1")
        self.btn2 = QPushButton(btnname + "2")
        self.btn3 = QPushButton(btnname + "3")
        self.setLayout(self.lay)
        self.lay.addWidget(self.btn1)
        self.lay.addWidget(self.btn2)
        self.lay.addWidget(self.btn3)


if __name__ == "__main__":
    qapp = QApplication(sys.argv)
    app = Widget()
    app.show()
    qapp.exec()

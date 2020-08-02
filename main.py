from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
import sys
from tabwidget import TabWidget
from widget import Widget1, Widget2, Widget3

class Main(QWidget):
    def __init__(self):
        super().__init__()
        wd1 = Widget1("Button 1")
        wd2 = Widget2("Button 2")
        wd3 = Widget3("Button 3")

        self.tw = TabWidget()
        self.tw.tabEmptySignal.connect(self.tabIsEmpty)
        self.tw.attachWidget(wd1, "WD1")
        self.tw.attachWidget(wd2, "WD2")
        self.tw.attachWidget(wd3, "WD3")
        self.tw.show()

    def tabIsEmpty(self):
        wd1 = Widget1("Button 111")
        self.tw.attachWidget(wd1, "New")

if __name__ == "__main__":
    qapp = QApplication(sys.argv)
    app = Main()
    qapp.exec()
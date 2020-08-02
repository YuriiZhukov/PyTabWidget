from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QTabWidget, QApplication, QMenu, QAction, QWidget
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QCursor
import sys
from widget import Widget1, Widget2, Widget3

class ITabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.menu = QMenu()
        self.attachAction = QAction("Attach")
        self.detachAction = QAction("Detach")

    def addAttachActions(self):
        self.menu.clear()
        self.menu.addAction(self.attachAction)

    def addDetachActions(self):
        self.menu.clear()
        self.menu.addAction(self.detachAction)

class TabWidget(ITabWidget):
    tabEmptySignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        # Структура, хранящая добавленные виджеты в Таб
        self.widgets = dict()
        self.tabs = dict()
        self.addDetachActions()
        self.setMovable(True)
        self.detachAction.triggered.connect(lambda : self.detachWidget(
                                            self.widgets[id(self.currentWidget())][0]
                                            ))

    # Прикрепление виджета к главному окну
    def attachWidget(self, widget, name):
        self.addTab(widget, name)
        self.widgets[id(widget)] = [widget, name]

    # Открепление виджета от главного окна
    def detachWidget(self, widget):
        detachedTab = DetachedTabWidget(self)
        detachedTab.addTab(widget, self.widgets[id(widget)][1])
        detachedTab.show()
        detachedTab.closeEvent = lambda x : self.close(detachedTab)
        self.tabs[id(detachedTab)] = detachedTab
        del self.widgets[id(widget)]
        if (len(self.widgets) == 0):
            self.tabEmptySignal.emit()


    def close(self, detachedTab):
        del self.tabs[id(detachedTab)]
        # print("Attached = ", len(self.widgets))
        # print("Detached = ", len(self.tabs))
        # print("----------------------")

    def openInNewTab(self):
        self.addTab(self.emptyWidgetRef, self.emptyWidgetName)

    def currentWidgetID(self):
        return id(self.currentWidget())

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.setCurrentIndex(self.tabBar().tabAt(QWidget().mapFromGlobal(a0.pos())))
        if a0.type() == Qt.RightButton:
            self.menu.exec(QCursor.pos())

class DetachedTabWidget(ITabWidget):
    def __init__(self, parentTab):
        super().__init__()
        self.parentTab = parentTab
        self.addAttachActions()
        self.attachAction.triggered.connect(self.attachWidget)

    # Прикрепление виджета к главному окну
    def attachWidget(self):
        del self.parentTab.tabs[id(self)]
        self.parentTab.attachWidget(self.currentWidget(), self.tabText(self.currentIndex()))
        self.deleteLater()


    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        if a0.type() == Qt.RightButton:
            self.menu.exec(QCursor.pos())


if __name__ == "__main__":
    qapp = QApplication(sys.argv)
    app = TabWidget()
    app.show()
    qapp.exec()

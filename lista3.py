# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lista3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Youbook(object):
    def setupUi(self, Youbook):
        Youbook.setObjectName("Youbook")
        Youbook.resize(784, 598)
        Youbook.setMinimumSize(QtCore.QSize(784, 598))
        Youbook.setMaximumSize(QtCore.QSize(784, 598))
        Youbook.setStyleSheet("background-color: rgb(248, 120, 120);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);")
        Youbook.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(Youbook)
        self.centralwidget.setObjectName("centralwidget")
        self.jakiuzytkownik = QtWidgets.QLabel(self.centralwidget)
        self.jakiuzytkownik.setGeometry(QtCore.QRect(580, 0, 191, 41))
        self.jakiuzytkownik.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.01 rgba(255, 112, 112, 255), stop:1 rgba(255, 255, 255, 255));")
        self.jakiuzytkownik.setObjectName("jakiuzytkownik")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 60, 761, 491))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 759, 489))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 761, 491))
        self.listWidget.setMinimumSize(QtCore.QSize(761, 491))
        self.listWidget.setMaximumSize(QtCore.QSize(761, 491))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setMouseTracking(False)
        self.listWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.listWidget.setAcceptDrops(True)
        self.listWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.01 rgba(255, 112, 112, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-color: rgb(170, 0, 0);\n"
"gridline-color: rgb(170, 0, 0);")
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listWidget.setMidLineWidth(1)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.listWidget.setAlternatingRowColors(False)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        for i in range(0,100,1):
            item.setCheckState(QtCore.Qt.Unchecked)
            self.listWidget.addItem(item)
            item = QtWidgets.QListWidgetItem()

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 91, 23))
        self.pushButton.setObjectName("pushButton")
        Youbook.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Youbook)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 784, 21))
        self.menubar.setObjectName("menubar")
        self.menuWype_nij_formularz = QtWidgets.QMenu(self.menubar)
        self.menuWype_nij_formularz.setObjectName("menuWype_nij_formularz")
        self.menuFormularz = QtWidgets.QMenu(self.menuWype_nij_formularz)
        self.menuFormularz.setObjectName("menuFormularz")
        Youbook.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Youbook)
        self.statusbar.setObjectName("statusbar")
        Youbook.setStatusBar(self.statusbar)
        self.Twojalista = QtWidgets.QAction(Youbook)
        self.Twojalista.setObjectName("Twojalista")
        self.Wyloguj = QtWidgets.QAction(Youbook)
        self.Wyloguj.setObjectName("Wyloguj")
        self.Nowy = QtWidgets.QAction(Youbook)
        self.Nowy.setObjectName("Nowy")
        self.Popraw = QtWidgets.QAction(Youbook)
        self.Popraw.setObjectName("Popraw")
        self.Zamknij = QtWidgets.QAction(Youbook)
        self.Zamknij.setObjectName("Zamknij")
        self.menuFormularz.addAction(self.Nowy)
        self.menuFormularz.addAction(self.Popraw)
        self.menuWype_nij_formularz.addAction(self.menuFormularz.menuAction())
        self.menuWype_nij_formularz.addAction(self.Twojalista)
        self.menuWype_nij_formularz.addSeparator()
        self.menuWype_nij_formularz.addAction(self.Wyloguj)
        self.menuWype_nij_formularz.addAction(self.Zamknij)
        self.menubar.addAction(self.menuWype_nij_formularz.menuAction())

        self.retranslateUi(Youbook)
        QtCore.QMetaObject.connectSlotsByName(Youbook)

    def retranslateUi(self, Youbook):
        _translate = QtCore.QCoreApplication.translate
        Youbook.setWindowTitle(_translate("Youbook", "MainWindow"))
        self.jakiuzytkownik.setText(_translate("Youbook", "Użytkownik:"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        for i in range(0,100,1):
            item = self.listWidget.item(i)
            item.setText(_translate("Youbook", "Autor- Tytuł"))

        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Youbook", "Zatwierdz zmiany"))
        self.menuWype_nij_formularz.setTitle(_translate("Youbook", "Menu"))
        self.menuFormularz.setTitle(_translate("Youbook", "Fomularz"))
        self.Twojalista.setText(_translate("Youbook", "Twoja lista"))
        self.Wyloguj.setText(_translate("Youbook", "Wyloguj"))
        self.Nowy.setText(_translate("Youbook", "Nowy formularz"))
        self.Popraw.setText(_translate("Youbook", "Popraw swój formularz"))
        self.Zamknij.setText(_translate("Youbook", "Zamknij"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Youbook = QtWidgets.QMainWindow()
    ui = Ui_Youbook()
    ui.setupUi(Youbook)
    Youbook.show()
    sys.exit(app.exec_())


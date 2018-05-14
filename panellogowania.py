from PyQt5 import QtCore, QtGui, QtWidgets
from przywitanie1 import Ui_Youbook
from panelrejestracji import Ui_panelrejestracji
#import time
import sqlite3

class Ui_PanelLogowania(object):

    def openYoubook(self):
        self.welcomewindow = QtWidgets.QMainWindow()
        self.ui     = Ui_Youbook()
        self.ui.setupUi(self.welcomewindow)
        self.welcomewindow.show()


    def openWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui     = Ui_panelrejestracji()
        self.ui.setupUi(self.window)
        self.window.show()

    def sprawdzlogin(self):
        connection = sqlite3.connect("login.db")
        username   = self.wpisanyLogin.text()
        password   = self.wpisanyHaslo.text()
        email      = self.wpisanyAdresEmail.text()
        result     = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND EMAIL = ? AND PASSWORD = ?",(username,email,password))
        if(len(result.fetchall())>0):
            print("znaleziono uzytkownika")
            connection.execute("UPDATE USERS SET ZALOGOWANY=(?) WHERE ZALOGOWANY=(?);",("0","1"))
            #print("pierwsze zrobione")
            result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND EMAIL = ? AND PASSWORD = ?",
                                        (username, email, password))
            for nazwa in result:
                connection.execute("UPDATE USERS SET ZALOGOWANY=(?) WHERE USERNAME=(?);",("1",nazwa[0]))
                #time.sleep(1)
            connection.commit()
            connection.close()
            PanelLogowania.hide()
            self.openYoubook()

        else:
            print('nie znaleziono')
            connection.commit()
            connection.close()

    def setupUi(self, PanelLogowania):
        PanelLogowania.setObjectName("PanelLogowania")
        PanelLogowania.resize(569, 340)
        PanelLogowania.setStyleSheet("\n"
"background-color: rgb(248, 120, 120);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(PanelLogowania)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.NapisPanelLogowania = QtWidgets.QLabel(PanelLogowania)
        self.NapisPanelLogowania.setMinimumSize(QtCore.QSize(551, 45))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.NapisPanelLogowania.setFont(font)
        self.NapisPanelLogowania.setMouseTracking(False)
        self.NapisPanelLogowania.setAlignment(QtCore.Qt.AlignCenter)
        self.NapisPanelLogowania.setObjectName("NapisPanelLogowania")
        self.verticalLayout_3.addWidget(self.NapisPanelLogowania)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Napislogin = QtWidgets.QLabel(PanelLogowania)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Napislogin.setFont(font)
        self.Napislogin.setObjectName("Napislogin")
        self.verticalLayout.addWidget(self.Napislogin, 0, QtCore.Qt.AlignRight)
        self.napisadresemail = QtWidgets.QLabel(PanelLogowania)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.napisadresemail.setFont(font)
        self.napisadresemail.setObjectName("napisadresemail")
        self.verticalLayout.addWidget(self.napisadresemail, 0, QtCore.Qt.AlignRight)
        self.napishaslo = QtWidgets.QLabel(PanelLogowania)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.napishaslo.setFont(font)
        self.napishaslo.setObjectName("napishaslo")
        self.verticalLayout.addWidget(self.napishaslo, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.wpisanyLogin = QtWidgets.QLineEdit(PanelLogowania)
        self.wpisanyLogin.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.wpisanyLogin.setObjectName("wpisanyLogin")
        self.verticalLayout_2.addWidget(self.wpisanyLogin)
        self.wpisanyAdresEmail = QtWidgets.QLineEdit(PanelLogowania)
        self.wpisanyAdresEmail.setStyleSheet("\n"
"gridline-color: rgb(255, 74, 207);\n"
"border-color: rgb(248, 120, 120);\n"
"background-color: rgb(255, 255, 255);")
        self.wpisanyAdresEmail.setObjectName("wpisanyAdresEmail")
        self.verticalLayout_2.addWidget(self.wpisanyAdresEmail)
        self.wpisanyHaslo = QtWidgets.QLineEdit(PanelLogowania)
        self.wpisanyHaslo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.wpisanyHaslo.setObjectName("wpisanyHaslo")
        self.verticalLayout_2.addWidget(self.wpisanyHaslo)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.przyciskRejestracja = QtWidgets.QPushButton(PanelLogowania)
        self.przyciskRejestracja.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.01 rgba(255, 112, 112, 255), stop:1 rgba(0, 0, 0, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.01 rgba(255, 112, 112, 255), stop:1 rgba(255, 255, 255, 255));")
        self.przyciskRejestracja.setObjectName("przyciskRejestracja")

        self.przyciskRejestracja.clicked.connect(self.openWindow)

        self.horizontalLayout_2.addWidget(self.przyciskRejestracja)
        self.przyciskZaloguj = QtWidgets.QPushButton(PanelLogowania)
        self.przyciskZaloguj.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.01 rgba(255, 112, 112, 255), stop:1 rgba(255, 255, 255, 255));")
        self.przyciskZaloguj.setObjectName("przyciskZaloguj")
        self.przyciskZaloguj.clicked.connect(self.sprawdzlogin)
        self.horizontalLayout_2.addWidget(self.przyciskZaloguj)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(PanelLogowania)
        QtCore.QMetaObject.connectSlotsByName(PanelLogowania)

    def retranslateUi(self, PanelLogowania):
        _translate = QtCore.QCoreApplication.translate
        PanelLogowania.setWindowTitle(_translate("PanelLogowania", "BOOK&YOU"))
        self.NapisPanelLogowania.setText(_translate("PanelLogowania", "PANEL LOGOWANIA"))
        self.Napislogin.setText(_translate("PanelLogowania", "LOGIN"))
        self.napisadresemail.setText(_translate("PanelLogowania", "ADRES E-MAIL"))
        self.napishaslo.setText(_translate("PanelLogowania", "HASŁO"))
        self.przyciskRejestracja.setText(_translate("PanelLogowania", "Nowy użytkownik"))
        self.przyciskZaloguj.setText(_translate("PanelLogowania", "Zaloguj"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PanelLogowania = QtWidgets.QWidget()
    ui = Ui_PanelLogowania()
    ui.setupUi(PanelLogowania)
    PanelLogowania.show()
    sys.exit(app.exec_())


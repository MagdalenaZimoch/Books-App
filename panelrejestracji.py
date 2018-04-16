# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'panelrejestracji.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_panelrejestracji(object):
    def saveuser(self):
        username = self.wpisanyLogin.text()
        password = self.wpisanyHaslo.text()
        email = self.wpisanyAdresEmail.text()
        password2 = self.wpisanyPowtorzHaslo.text()
        #łączymy się z bazą danych
        connection = sqlite3.connect("login.db")
        # sprawdzamy czy podany login jest juz w baze danych
        result = connection.execute("SELECT * FROM USERS")
        print(result)
        taken = 0
        for data in result:
            print(data[0])
            if (username == data[0]):
                print("znaleziono uzytkownika o takiej samej nazwie, zmień login !")
                taken = 1
                break
            else:
                print('NIE ZNALEZIONO')
        if (taken == 0):
            if (password == password2):
                connection.execute("INSERT INTO USERS VALUES (?,?,?)", (username, email, password))
                connection.commit()
                print("DODANO UŻYTKOWNIKA")

            else:
                print('PODANE HASŁA NIE SĄ TAKIE SAME !')
        connection.close()



    def setupUi(self, panelrejestracji):
        panelrejestracji.setObjectName("panelrejestracji")
        panelrejestracji.resize(568, 447)
        panelrejestracji.setStyleSheet("background-color: rgb(248, 120, 120);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(panelrejestracji)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.napisRejestracja = QtWidgets.QLabel(panelrejestracji)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.napisRejestracja.setFont(font)
        self.napisRejestracja.setAlignment(QtCore.Qt.AlignCenter)
        self.napisRejestracja.setObjectName("napisRejestracja")
        self.verticalLayout_3.addWidget(self.napisRejestracja)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Napislogin = QtWidgets.QLabel(panelrejestracji)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Napislogin.setFont(font)
        self.Napislogin.setObjectName("Napislogin")
        self.verticalLayout.addWidget(self.Napislogin, 0, QtCore.Qt.AlignRight)
        self.napisadresemail = QtWidgets.QLabel(panelrejestracji)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.napisadresemail.setFont(font)
        self.napisadresemail.setObjectName("napisadresemail")
        self.verticalLayout.addWidget(self.napisadresemail, 0, QtCore.Qt.AlignRight)
        self.napishaslo = QtWidgets.QLabel(panelrejestracji)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.napishaslo.setFont(font)
        self.napishaslo.setObjectName("napishaslo")
        self.verticalLayout.addWidget(self.napishaslo, 0, QtCore.Qt.AlignRight)
        self.napisPowtorzHaslo = QtWidgets.QLabel(panelrejestracji)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.napisPowtorzHaslo.setFont(font)
        self.napisPowtorzHaslo.setObjectName("napisPowtorzHaslo")
        self.verticalLayout.addWidget(self.napisPowtorzHaslo)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.wpisanyLogin = QtWidgets.QLineEdit(panelrejestracji)
        self.wpisanyLogin.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.wpisanyLogin.setObjectName("wpisanyLogin")
        self.verticalLayout_2.addWidget(self.wpisanyLogin)
        self.wpisanyAdresEmail = QtWidgets.QLineEdit(panelrejestracji)
        self.wpisanyAdresEmail.setStyleSheet("\n"
"gridline-color: rgb(255, 74, 207);\n"
"border-color: rgb(248, 120, 120);\n"
"background-color: rgb(255, 255, 255);")
        self.wpisanyAdresEmail.setObjectName("wpisanyAdresEmail")
        self.verticalLayout_2.addWidget(self.wpisanyAdresEmail)
        self.wpisanyHaslo = QtWidgets.QLineEdit(panelrejestracji)
        self.wpisanyHaslo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.wpisanyHaslo.setObjectName("wpisanyHaslo")
        self.verticalLayout_2.addWidget(self.wpisanyHaslo)
        self.wpisanyPowtorzHaslo = QtWidgets.QLineEdit(panelrejestracji)
        self.wpisanyPowtorzHaslo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.wpisanyPowtorzHaslo.setObjectName("wpisanyPowtorzHaslo")
        self.verticalLayout_2.addWidget(self.wpisanyPowtorzHaslo)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.przyciskStworzUzytkownika = QtWidgets.QPushButton(panelrejestracji)
        self.przyciskStworzUzytkownika.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.01 rgba(255, 112, 112, 255), stop:1 rgba(255, 255, 255, 255));")
        self.przyciskStworzUzytkownika.setObjectName("przyciskStworzUzytkownika")

        #znikanie okna po dodaniu użytkownika do bazy

        self.przyciskStworzUzytkownika.clicked.connect(self.saveuser)
        self.verticalLayout_3.addWidget(self.przyciskStworzUzytkownika)

        self.retranslateUi(panelrejestracji)
        QtCore.QMetaObject.connectSlotsByName(panelrejestracji)

    def retranslateUi(self, panelrejestracji):
        _translate = QtCore.QCoreApplication.translate
        panelrejestracji.setWindowTitle(_translate("panelrejestracji", "PANEL REJESTRACJI"))
        self.napisRejestracja.setText(_translate("panelrejestracji", "STWÓRZ NOWE KONTO"))
        self.Napislogin.setText(_translate("panelrejestracji", "LOGIN"))
        self.napisadresemail.setText(_translate("panelrejestracji", "ADRES E-MAIL"))
        self.napishaslo.setText(_translate("panelrejestracji", "HASŁO"))
        self.napisPowtorzHaslo.setText(_translate("panelrejestracji", "POWTÓRZ HASŁO"))
        self.przyciskStworzUzytkownika.setText(_translate("panelrejestracji", "Stwórz użytkownika"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    panelrejestracji = QtWidgets.QWidget()
    ui = Ui_panelrejestracji()
    ui.setupUi(panelrejestracji)
    panelrejestracji.show()
    sys.exit(app.exec_())


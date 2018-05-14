# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formularz.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3

class Ui_Youbook(object):
    def openLista(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Youbookk()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Youbook):
        con = sqlite3.connect("login.db")
        zalogowany = con.execute('SELECT * FROM USERS WHERE ZALOGOWANY=1')
        for osoba in zalogowany:
            print(osoba[0])
            użytkownik=osoba[0]
        con.commit()
        con.close()
        def sprawdz(self):
            realne = self.checkState()
            print(realne)
            return realne
        def sprawdzwszystkie():
            connection = sqlite3.connect("formularze.db")
            ############# zapis danych do formularza ###########33

            connection.execute('UPDATE FORMULARZE SET REAL=? WHERE USERNAME=?;',(sprawdz(self.p_realne),użytkownik))
            print("realna:")
            sprawdz(self.p_realne)

            connection.execute('UPDATE FORMULARZE SET FANTASTIC=? WHERE USERNAME=?;', (sprawdz(self.p_fantastyczne), użytkownik))
            print("fantastyczna")
            sprawdz(self.p_fantastyczne)

            connection.execute('UPDATE FORMULARZE SET FACTS=? WHERE USERNAME=?;', (sprawdz(self.p_opartanafaktach), użytkownik))
            print("oparta na faktach")
            sprawdz(self.p_opartanafaktach)

            connection.execute('UPDATE FORMULARZE SET BRAKROZDZIALY=? WHERE USERNAME=?;', (sprawdz(self.p_brakrozdzialu), użytkownik))
            print("brak podziału na rozdziały")
            sprawdz(self.p_brakrozdzialu)

            connection.execute('UPDATE FORMULARZE SET ROZDZIALY=? WHERE USERNAME=?;', (sprawdz(self.p_rozdzialy), użytkownik))
            print("jest podział na rozdziały")
            sprawdz(self.p_rozdzialy)

            connection.execute('UPDATE FORMULARZE SET GLOWNYKOBIETA=? WHERE USERNAME=?;', (sprawdz(self.p_glownybohaterkobieta), użytkownik))
            print("głównym bohaterem jest kobieta")
            sprawdz(self.p_glownybohaterkobieta)

            connection.execute('UPDATE FORMULARZE SET GLOWNYMEZCZYZNA=? WHERE USERNAME=?;', (sprawdz(self.p_glownybohatermezczyzna), użytkownik))
            print("głównym bohaterem jest mężczyzna")
            sprawdz(self.p_glownybohatermezczyzna)

            connection.execute('UPDATE FORMULARZE SET NARRATOR1=? WHERE USERNAME=?;',(sprawdz(self.p_narrator1), użytkownik))
            print("narrator 1os")
            sprawdz(self.p_narrator1)

            connection.execute('UPDATE FORMULARZE SET NARRATOR3=? WHERE USERNAME=?;', (sprawdz(self.p_narrator3), użytkownik))
            print("narrator 3os")
            sprawdz(self.p_narrator3)

            connection.execute('UPDATE FORMULARZE SET PAUTOR=? WHERE USERNAME=?;', (sprawdz(self.p_polskiautor), użytkownik))
            print("autor jest polakiem")
            sprawdz(self.p_polskiautor)

            connection.execute('UPDATE FORMULARZE SET ZAUTOR=? WHERE USERNAME=?;', (sprawdz(self.p_zagranicznyautor), użytkownik))
            print("autor jest zagraniczny")
            sprawdz(self.p_zagranicznyautor)

            connection.execute('UPDATE FORMULARZE SET CZASPRZESZLOSC=? WHERE USERNAME=?;', (sprawdz(self.p_przeszlosc), użytkownik))
            print("czas akcji - przeszłość")
            sprawdz(self.p_przeszlosc)

            connection.execute('UPDATE FORMULARZE SET CZASPRZYSZLOSC=? WHERE USERNAME=?;', (sprawdz(self.p_przyszlosc), użytkownik))
            print("czas akcji przyszłość")
            sprawdz(self.p_przyszlosc)

            connection.execute('UPDATE FORMULARZE SET CZASTERAZ=? WHERE USERNAME=?;', (sprawdz(self.p_terazniejszosc), użytkownik))
            print("czas akcji teraźniejszośc")
            sprawdz(self.p_terazniejszosc)

            connection.execute('UPDATE FORMULARZE SET TFANTASTYCZNA=? WHERE USERNAME=?;', (sprawdz(self.t_fantastyczna), użytkownik))
            print("fantastyczna")
            sprawdz(self.t_fantastyczna)

            connection.execute('UPDATE FORMULARZE SET TFANTASTYCZNONAUKOWA=? WHERE USERNAME=?;',(sprawdz(self.t_fantastycznonaukowa), użytkownik))
            print("fantastycznonaukowa")
            sprawdz(self.t_fantastycznonaukowa)

            connection.execute('UPDATE FORMULARZE SET TGOTYCKA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_gotycka), użytkownik))
            print("gotycka")
            sprawdz(self.t_gotycka)

            connection.execute('UPDATE FORMULARZE SET THISTORYCZNA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_historyczna), użytkownik))
            print("historyczna")
            sprawdz(self.t_historyczna)

            connection.execute('UPDATE FORMULARZE SET TKRYMINALNA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_kryminalna), użytkownik))
            print("kryminalna")
            sprawdz(self.t_kryminalna)

            connection.execute('UPDATE FORMULARZE SET TLOTRZYSKOWSKA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_lotrzyskowska), użytkownik))
            print("łotrzyskowska")
            sprawdz(self.t_lotrzyskowska)

            connection.execute('UPDATE FORMULARZE SET TMARYNISTYCZNA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_marynistyczna), użytkownik))
            print("marynistyczna")
            sprawdz(self.t_marynistyczna)

            connection.execute('UPDATE FORMULARZE SET TPRODUKCYJNA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_produkcyjna), użytkownik))
            print("produkcyjna")
            sprawdz(self.t_produkcyjna)

            connection.execute('UPDATE FORMULARZE SET TPRZYGODOWA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_przygodowa), użytkownik))
            print("przygodowa")
            sprawdz(self.t_przygodowa)

            connection.execute('UPDATE FORMULARZE SET TPSYCHOLOGICZNA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_psychologiczna), użytkownik))
            print("psychologiczna")
            sprawdz(self.t_psychologiczna)

            connection.execute('UPDATE FORMULARZE SET TSENSACYJNA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_sensacyjna), użytkownik))
            print("sensacyjna")
            sprawdz(self.t_sensacyjna)

            connection.execute('UPDATE FORMULARZE SET TSENTYMENTALNA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_sentymentalna), użytkownik))
            print("sentymentalna")
            sprawdz(self.t_sentymentalna)

            connection.execute('UPDATE FORMULARZE SET TSPOLECZNOOBYCZAJOWA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_spolecznoobyczajowa), użytkownik))
            print("społecznoobyczajowa")
            sprawdz(self.t_spolecznoobyczajowa)

            connection.execute('UPDATE FORMULARZE SET AUTOR=? WHERE USERNAME=?;',
                               (self.ulubionyautor.currentText(), użytkownik))
            print("Twój ulubiony autor:")
            print(self.ulubionyautor.currentText())

            connection.execute('UPDATE FORMULARZE SET WIEK=? WHERE USERNAME=?;',
                               (self.wiek.currentText(), użytkownik))
            print("Twój wiek")
            print(self.wiek.currentText())

            connection.execute('UPDATE FORMULARZE SET ILOSCSTRON=? WHERE USERNAME=?;',
                               (self.iloscstron.currentText(), użytkownik))
            print("Ile stron ma mieć książka:")
            print(self.iloscstron.currentText())

            connection.execute('UPDATE FORMULARZE SET JEZYK=? WHERE USERNAME=?;',
                               (self.jezykksiazki.currentText(), użytkownik))
            print("W jakim jezyku ma byc ksiazka:")
            print(self.jezykksiazki.currentText())

            connection.commit()
            connection.close()


        Youbook.setObjectName("Youbook")
        Youbook.resize(784, 598)
        Youbook.setStyleSheet("background-color: rgb(248, 120, 120);\n"
"selection-color: rgb(255, 255, 255);")

        self.centralwidget = QtWidgets.QWidget(Youbook)

        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 175, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.p_realne = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.p_realne.setObjectName("p_realne")
        self.verticalLayout.addWidget(self.p_realne)


        self.p_fantastyczne = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.p_fantastyczne.setObjectName("p_fantastyczne")
        self.verticalLayout.addWidget(self.p_fantastyczne)


        self.p_opartanafaktach = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.p_opartanafaktach.setObjectName("p_opartanafaktach")
        self.verticalLayout.addWidget(self.p_opartanafaktach)
        self.p_narrator1 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.p_narrator1.setObjectName("p_narrator1")
        self.verticalLayout.addWidget(self.p_narrator1)
        self.p_narrator3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.p_narrator3.setObjectName("p_narrator3")
        self.verticalLayout.addWidget(self.p_narrator3)
        self.p_polskiautor = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.p_polskiautor.setObjectName("p_polskiautor")
        self.verticalLayout.addWidget(self.p_polskiautor)
        self.p_zagranicznyautor = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.p_zagranicznyautor.setObjectName("p_zagranicznyautor")
        self.verticalLayout.addWidget(self.p_zagranicznyautor)
        self.p_glownybohaterkobieta = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.p_glownybohaterkobieta.setObjectName("p_glownybohaterkobieta")
        self.verticalLayout.addWidget(self.p_glownybohaterkobieta)
        self.p_glownybohatermezczyzna = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.p_glownybohatermezczyzna.setObjectName("p_glownybohatermezczyzna")
        self.verticalLayout.addWidget(self.p_glownybohatermezczyzna)
        self.p_terazniejszosc = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.p_terazniejszosc.setObjectName("p_terazniejszosc")
        self.verticalLayout.addWidget(self.p_terazniejszosc)
        self.p_przyszlosc = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.p_przyszlosc.setObjectName("p_przyszlosc")
        self.verticalLayout.addWidget(self.p_przyszlosc)
        self.p_przeszlosc = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.p_przeszlosc.setObjectName("p_przeszlosc")
        self.verticalLayout.addWidget(self.p_przeszlosc)
        self.p_rozdzialy = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.p_rozdzialy.setObjectName("p_rozdzialy")
        self.verticalLayout.addWidget(self.p_rozdzialy)
        self.p_brakrozdzialu = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.p_brakrozdzialu.setObjectName("p_brakrozdzialu")
        self.verticalLayout.addWidget(self.p_brakrozdzialu)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 201, 16))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(210, 40, 160, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.wiek = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.wiek.setAutoFillBackground(False)
        self.wiek.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.wiek.setObjectName("wiek")
        for i in range(0,101,1):
            self.wiek.addItem("")



        self.wiek.setItemText(64, "")
        self.horizontalLayout.addWidget(self.wiek)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(210, 90, 160, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.iloscstron = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.iloscstron.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.iloscstron.setObjectName("iloscstron")
        self.iloscstron.addItem("")
        self.iloscstron.addItem("")
        self.iloscstron.addItem("")
        self.horizontalLayout_2.addWidget(self.iloscstron)
        self.Cancel = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.Cancel.setGeometry(QtCore.QRect(620, 530, 156, 23))
        self.Cancel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.01 rgba(255, 112, 112, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Cancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.Cancel.setObjectName("Cancel")

        self.Cancel.accepted.connect(sprawdzwszystkie)
        #self.Cancel.accepted.connect(self.openLista())
        self.Cancel.rejected.connect(sprawdzwszystkie)



        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(210, 140, 258, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.jezykksiazki = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.jezykksiazki.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.jezykksiazki.setObjectName("jezykksiazki")
        self.jezykksiazki.addItem("")

        ################# liczba miejsc na języki ###########
        connection = sqlite3.connect("books.db")
        result = connection.execute("SELECT JEZYK FROM BOOKS")
        lista = []
        for data in result:
            lista.append(data)
        lista = list(set(lista))
        for data in lista:
            self.jezykksiazki.addItem("")
        connection.commit()
        connection.close()
        ######################################################

        self.horizontalLayout_3.addWidget(self.jezykksiazki)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(210, 190, 311, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.ulubionyautor = QtWidgets.QComboBox(self.horizontalLayoutWidget_5)
        self.ulubionyautor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ulubionyautor.setObjectName("ulubionyautor")
        self.ulubionyautor.addItem("")
        ###################### liczba miejsc na autorow #############################
        connection = sqlite3.connect("books.db")
        result = connection.execute("SELECT AUTOR FROM BOOKS")

        lista = []
        for data in result:
            lista.append(data)
        lista = list(set(lista))
        for data in lista:
            self.ulubionyautor.addItem("")
        connection.commit()
        connection.close()
        #####################################################################################
        ############### wyciaganie autora #######################

        print(self.ulubionyautor.show())





        self.ulubionyautor.setItemText(64, "")
        self.horizontalLayout_5.addWidget(self.ulubionyautor)
        self.jakiuzytkownik = QtWidgets.QLabel(self.centralwidget)
        self.jakiuzytkownik.setGeometry(QtCore.QRect(580, 0, 191, 41))
        self.jakiuzytkownik.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.01 rgba(255, 112, 112, 255), stop:1 rgba(255, 255, 255, 255));")
        self.jakiuzytkownik.setObjectName("jakiuzytkownik")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(380, 50, 362, 41))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.b_starszy = QtWidgets.QRadioButton(self.horizontalLayoutWidget_7)
        self.b_starszy.setObjectName("b_starszy")
        self.horizontalLayout_7.addWidget(self.b_starszy)
        self.b_mlodszy = QtWidgets.QRadioButton(self.horizontalLayoutWidget_7)
        self.b_mlodszy.setObjectName("b_mlodszy")
        self.horizontalLayout_7.addWidget(self.b_mlodszy)
        self.b_wwieku = QtWidgets.QRadioButton(self.horizontalLayoutWidget_7)
        self.b_wwieku.setObjectName("b_wwieku")
        self.horizontalLayout_7.addWidget(self.b_wwieku)
        self.b_obojetnie = QtWidgets.QRadioButton(self.horizontalLayoutWidget_7)
        self.b_obojetnie.setObjectName("b_obojetnie")


        self.horizontalLayout_7.addWidget(self.b_obojetnie)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(380, 40, 121, 16))
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 250, 91, 16))
        self.label_5.setObjectName("label_5")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(220, 270, 161, 282))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.t_sensacyjna = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.t_sensacyjna.setObjectName("t_sensacyjna")
        self.gridLayout.addWidget(self.t_sensacyjna, 10, 0, 1, 1)
        self.t_przygodowa = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.t_przygodowa.setObjectName("t_przygodowa")
        self.gridLayout.addWidget(self.t_przygodowa, 8, 0, 1, 1)
        self.t_fantastyczna = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.t_fantastyczna.setTristate(False)
        self.t_fantastyczna.setObjectName("t_fantastyczna")
        self.gridLayout.addWidget(self.t_fantastyczna, 0, 0, 1, 1)
        self.t_produkcyjna = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.t_produkcyjna.setObjectName("t_produkcyjna")
        self.gridLayout.addWidget(self.t_produkcyjna, 7, 0, 1, 1)
        self.t_lotrzyskowska = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.t_lotrzyskowska.setObjectName("t_lotrzyskowska")
        self.gridLayout.addWidget(self.t_lotrzyskowska, 5, 0, 1, 1)
        self.t_psychologiczna = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.t_psychologiczna.setObjectName("t_psychologiczna")
        self.gridLayout.addWidget(self.t_psychologiczna, 9, 0, 1, 1)
        self.t_kryminalna = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.t_kryminalna.setObjectName("t_kryminalna")
        self.gridLayout.addWidget(self.t_kryminalna, 4, 0, 1, 1)
        self.t_historyczna = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.t_historyczna.setObjectName("t_historyczna")
        self.gridLayout.addWidget(self.t_historyczna, 3, 0, 1, 1)
        self.t_fantastycznonaukowa = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.t_fantastycznonaukowa.setObjectName("t_fantastycznonaukowa")
        self.gridLayout.addWidget(self.t_fantastycznonaukowa, 1, 0, 1, 1)
        self.t_gotycka = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.t_gotycka.setObjectName("t_gotycka")
        self.gridLayout.addWidget(self.t_gotycka, 2, 0, 1, 1)
        self.t_marynistyczna = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.t_marynistyczna.setObjectName("t_marynistyczna")
        self.gridLayout.addWidget(self.t_marynistyczna, 6, 0, 1, 1)
        self.t_sentymentalna = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.t_sentymentalna.setObjectName("t_sentymentalna")
        self.gridLayout.addWidget(self.t_sentymentalna, 11, 0, 1, 1)
        self.t_spolecznoobyczajowa = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.t_spolecznoobyczajowa.setObjectName("t_spolecznoobyczajowa")
        self.gridLayout.addWidget(self.t_spolecznoobyczajowa, 12, 0, 1, 1)



        ####### menu ###########
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
        Youbook.setWindowTitle(_translate("Youbook", "BOOK&YOU"))
        self.p_realne.setText(_translate("Youbook", "Postacie realne"))
        self.p_fantastyczne.setText(_translate("Youbook", "Postacie fantastyczne"))
        self.p_opartanafaktach.setText(_translate("Youbook", "Książka oparta na faktach"))
        self.p_narrator1.setText(_translate("Youbook", "Narrator 1 osobowy"))
        self.p_narrator3.setText(_translate("Youbook", "Narrator 3 osobowy"))
        self.p_polskiautor.setText(_translate("Youbook", "Polski autor"))
        self.p_zagranicznyautor.setText(_translate("Youbook", "Zagraniczny autor"))
        self.p_glownybohaterkobieta.setText(_translate("Youbook", "Główny bohater jest płci żeńskiej"))
        self.p_glownybohatermezczyzna.setText(_translate("Youbook", "Główny bohater jest płci męskiej"))
        self.p_terazniejszosc.setText(_translate("Youbook", "Czas akcji-Teraźniejszość"))
        self.p_przyszlosc.setText(_translate("Youbook", "Czas akcji-Przyszłość"))
        self.p_przeszlosc.setText(_translate("Youbook", "Czas akcji-Przeszłość"))
        self.p_rozdzialy.setText(_translate("Youbook", "Podzielona na rozdziały"))
        self.p_brakrozdzialu.setText(_translate("Youbook", "Brak podziału na rozdziały"))
        self.label.setText(_translate("Youbook", "Zaznacz rzeczy które lubisz w książkach:"))
        self.label_2.setText(_translate("Youbook", "Podaj swój wiek"))
        for i in range(0,101,1):
            self.wiek.setItemText(i, _translate("Youbook", str(i)))

        self.label_3.setText(_translate("Youbook", "Ilość stron"))
        self.iloscstron.setItemText(0, _translate("Youbook", "0-100"))
        self.iloscstron.setItemText(1, _translate("Youbook", "100-500"))
        self.iloscstron.setItemText(2, _translate("Youbook", "500-inf"))


        self.label_4.setText(_translate("Youbook", "Język na jaki zostala przetłumaczona"))
        self.jezykksiazki.setItemText(0, _translate("Youbook", "inny"))
        ####################################################################################
        connection = sqlite3.connect("books.db")
        result = connection.execute("SELECT JEZYK FROM BOOKS")
        i = 1
        lista = []
        for data in result:
            lista.append(data)
        lista = list(set(lista))
        for data in lista:
            self.jezykksiazki.setItemText(i, _translate("Youbook", data[0]))
            i = i + 1
        connection.commit()
        connection.close()
        ######################################################################################

        self.label_6.setText(_translate("Youbook", "Wybierz ulubionego autora z listy    "))
        self.ulubionyautor.setItemText(0, _translate("Youbook", "Nie mam "))
        ####################################################################################
        connection = sqlite3.connect("books.db")
        result = connection.execute("SELECT AUTOR FROM BOOKS")
        i=1
        lista=[]
        for data in result:
            lista.append(data)
        lista=list(set(lista))
        for data in lista:
            self.ulubionyautor.setItemText(i,_translate("Youbook",data[0]))
            i=i+1
        connection.commit()
        connection.close()
        #####################################################################################
        con = sqlite3.connect("login.db")
        zalogowany = con.execute('SELECT * FROM USERS WHERE ZALOGOWANY=1')
        for osoba in zalogowany:
            #print(osoba[0])
            użytkownik = osoba[0]
        con.commit()
        con.close()

        nazwa_użytkownika = "Użytkownik : " + str(użytkownik)
        self.jakiuzytkownik.setText(_translate("Youbook", nazwa_użytkownika))
        self.b_starszy.setText(_translate("Youbook", "Jest starszy"))
        self.b_mlodszy.setText(_translate("Youbook", "Jest młodszy"))
        self.b_wwieku.setText(_translate("Youbook", "Jest w Twoim wieku"))
        self.b_obojetnie.setText(_translate("Youbook", "Obojętnie"))
        self.label_9.setText(_translate("Youbook", "Lubisz jak bohater książki:"))
        self.label_5.setText(_translate("Youbook", "Tematyka:"))
        self.t_sensacyjna.setText(_translate("Youbook", "sensacyjna"))
        self.t_przygodowa.setText(_translate("Youbook", "przygodowa"))
        self.t_fantastyczna.setText(_translate("Youbook", "fantastyczna"))
        self.t_produkcyjna.setText(_translate("Youbook", "produkcyjna"))
        self.t_lotrzyskowska.setText(_translate("Youbook", "łotrzyskowska"))
        self.t_psychologiczna.setText(_translate("Youbook", "psychologiczna"))
        self.t_kryminalna.setText(_translate("Youbook", "kryminalna"))
        self.t_historyczna.setText(_translate("Youbook", "historyczna"))
        self.t_fantastycznonaukowa.setText(_translate("Youbook", "fantastyczno-naukowa"))
        self.t_gotycka.setText(_translate("Youbook", "gotycka"))
        self.t_marynistyczna.setText(_translate("Youbook", "marynistyczna"))
        self.t_sentymentalna.setText(_translate("Youbook", "sentymentalna"))
        self.t_spolecznoobyczajowa.setText(_translate("Youbook", "społeczno-obyczajowa"))
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


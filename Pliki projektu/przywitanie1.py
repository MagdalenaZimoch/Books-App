from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3
import time


class Ui_Youbook3(object):
    def setupUi(self, Youbook3):
        Youbook3.setObjectName("Youbook3")
        Youbook3.resize(784, 598)
        Youbook3.setMinimumSize(QtCore.QSize(784, 598))
        Youbook3.setMaximumSize(QtCore.QSize(784, 598))
        Youbook3.setStyleSheet("background-color: rgb(248, 120, 120);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);")
        Youbook3.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(Youbook3)
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

        ########## liczba elementów na liście ##########################################################################
        con = sqlite3.connect("login.db")
        zalogowany = con.execute('SELECT * FROM USERS WHERE ZALOGOWANY=1')
        for osoba in zalogowany:
            użytkownik=(osoba[0])

        con4 = sqlite3.connect("formularze.db")
        wyniki = con4.execute('SELECT * FROM FORMULARZE')
        for data in wyniki:
            if (data[0]==użytkownik):
                listaużytkownika=data[2]
                listazabroniona = list(data[33])

        nowalista = []
        i = 0
        while len(listaużytkownika)>i:
            liczba = ''
            if (listaużytkownika[i].isdigit()):
                liczba += listaużytkownika[i]
                ileel=1
                while (listaużytkownika[i + ileel].isdigit()):
                    liczba += (listaużytkownika[i + ileel])
                    nowalista.append(liczba)
                    ileel += 1

                else:
                    nowalista.append(liczba)
                    i += ileel
            else:
                i += 1

        m = 0
        dousuniecia = []
        while len(listazabroniona) > m:
            liczba = ''
            if (listazabroniona[m].isdigit()):
                liczba += listazabroniona[m]
                ileel = 1
                while (listazabroniona[m + ileel].isdigit()):
                    liczba += (listazabroniona[m + ileel])
                    dousuniecia.append(liczba)
                    ileel += 1

                else:
                    dousuniecia.append(liczba)
                    m += ileel
            else:
                m += 1

        dousuniecia=set(dousuniecia)
        nowalista = set(nowalista) - set(dousuniecia)

        for i in nowalista:
            if i=='0':
                continue
            else:

                item.setCheckState(QtCore.Qt.Unchecked)
                self.listWidget.addItem(item)
                item = QtWidgets.QListWidgetItem()

        ################################################################################################################

        ##################### sprawdza czy jej zaznaczony i nie usuwa ##################################################
        zaznaczone = []
        def sprawdz3():
            for index in range(self.listWidget.count()):
                if self.listWidget.item(index).checkState() == QtCore.Qt.Checked:
                    item = self.listWidget.item(index).text()
                    zaznaczone.append(item)


        def usun():
            con6 = sqlite3.connect("formularze.db")
            result = con6.execute('SELECT * FROM FORMULARZE')
            con7 = sqlite3.connect("books.db")
            spis = con7.execute('SELECT * FROM BOOKS')

            ##################kod pomocniczy############################################################################
            for data in result:
                if data[0]==użytkownik:
                    przeczytane1 = data[33]

            ############################################################################################################
            ###########################faktyczne usuwanie ##############################################################

            przeczytane=[]
            for data2 in zaznaczone:
                autor=''
                tyt=[]
                tytul=''
                i=0
                for a in data2:
                    while (data2[i+1]!='-'):
                        autor+=(data2[i])
                        i=i+1
                i=-1
                while (data2[i - 1] != '-'):
                    tyt.append(data2[i])
                    i = i - 1

                tyt.reverse()
                for i in tyt:
                    tytul+=i
                ################sprawdza jakie id ma zaznaczona książka  ###############################################
                for book in spis:
                    if(book[2]==tytul):
                        przeczytane.append(book[0])
                        break
                    continue

            #######################dodanie do bazy ksiązek przeczytanych ###############################################
            listaprzeczytanych = przeczytane1 + str(przeczytane)

            con6.execute("UPDATE FORMULARZE SET PRZECZYTANE=(?) WHERE USERNAME=(?);", (listaprzeczytanych, użytkownik))
            con6.commit()
            con6.close()
            con7.commit()
            con7.close()
        ################################################################################################################


        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 91, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.pressed.connect(sprawdz3)
        self.pushButton.pressed.connect(usun)


        Youbook3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Youbook3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 784, 21))
        self.menubar.setObjectName("menubar")
        self.menuWype_nij_formularz = QtWidgets.QMenu(self.menubar)
        self.menuWype_nij_formularz.setObjectName("menuWype_nij_formularz")
        self.menuFormularz = QtWidgets.QMenu(self.menuWype_nij_formularz)
        self.menuFormularz.setObjectName("menuFormularz")
        Youbook3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Youbook3)
        self.statusbar.setObjectName("statusbar")
        Youbook3.setStatusBar(self.statusbar)


        self.retranslateUi(Youbook3)
        QtCore.QMetaObject.connectSlotsByName(Youbook3)

    def retranslateUi(self, Youbook3):
        _translate = QtCore.QCoreApplication.translate
        Youbook3.setWindowTitle(_translate("Youbook3", "BOOK&YOU"))

        ###################################wyświetlanie zalogowanego użytkownika########################################
        con = sqlite3.connect("login.db")
        zalogowany = con.execute('SELECT * FROM USERS WHERE ZALOGOWANY=1')
        for osoba in zalogowany:
            użytkownik = osoba[0]
        con.commit()
        con.close()


        nazwa_użytkownika = "Użytkownik : " + str(użytkownik)
        self.jakiuzytkownik.setText(_translate("Youbook3", nazwa_użytkownika))
        ################################################################################################################

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)

        ############# sprawdzanie jaki autor i tytul ma byc wyswietlony na liście ######################################
        con4 = sqlite3.connect("formularze.db")
        wyniki = con4.execute('SELECT * FROM FORMULARZE')
        for data in wyniki:
            if (data[0] == użytkownik):
                listaużytkownika = list(data[2])
                listazabroniona = list(data[33])
        con4.commit()
        con4.close()

        nowalista = []
        i = 0
        while len(listaużytkownika) > i:
            liczba = ''
            if (listaużytkownika[i].isdigit()):
                liczba += listaużytkownika[i]
                ileel = 1
                while (listaużytkownika[i + ileel].isdigit()):
                    liczba += (listaużytkownika[i + ileel])
                    nowalista.append(liczba)
                    ileel += 1

                else:
                    nowalista.append(liczba)
                    i += ileel
            else:
                i += 1

        m=0
        dousuniecia=[]
        while len(listazabroniona) > m:
            liczba = ''
            if (listazabroniona[m].isdigit()):
                liczba += listazabroniona[m]
                ileel = 1
                while (listazabroniona[m + ileel].isdigit()):
                    liczba += (listazabroniona[m + ileel])
                    dousuniecia.append(liczba)
                    ileel += 1

                else:
                    dousuniecia.append(liczba)
                    m += ileel
            else:
                m += 1


        dousuniecia = set(dousuniecia)
        nowalista=set(nowalista)-set(dousuniecia)



        con5 = sqlite3.connect("books.db")
        wyniki5 = con5.execute('SELECT * FROM BOOKS')

        numer = 0
        for data in wyniki5:
            for el in nowalista:
                if int(el) == data[0]:
                    item = self.listWidget.item(numer)
                    autor = data[1]
                    tytul = data[2]
                    item.setText(_translate("Youbook3", autor + ' - ' + tytul))
                    numer=numer+1

        ################################################################################################################

        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Youbook3", "Zatwierdz zmiany"))


class Ui_Youbook(object):
    def setupUi(self, Youbook):
        con = sqlite3.connect("login.db")
        zalogowany = con.execute('SELECT * FROM USERS WHERE ZALOGOWANY=1')
        for osoba in zalogowany:
            użytkownik = osoba[0]
        con.commit()
        con.close()
        ########### funkcja, która sprawdza co zostało zaznaczone ######################################################
        def sprawdz(self):
            wynik = self.checkState()
            return wynik

        def sprawdzwszystkie():

            connection = sqlite3.connect("formularze.db")
            ############# zapis danych do formularza ###################################################################

            connection.execute('UPDATE FORMULARZE SET REAL=? WHERE USERNAME=?;', (sprawdz(self.p_realne), użytkownik))
            sprawdz(self.p_realne)

            connection.execute('UPDATE FORMULARZE SET FANTASTIC=? WHERE USERNAME=?;',
                               (sprawdz(self.p_fantastyczne), użytkownik))
            sprawdz(self.p_fantastyczne)

            connection.execute('UPDATE FORMULARZE SET FACTS=? WHERE USERNAME=?;',
                               (sprawdz(self.p_opartanafaktach), użytkownik))
            sprawdz(self.p_opartanafaktach)

            connection.execute('UPDATE FORMULARZE SET BRAKROZDZIALY=? WHERE USERNAME=?;',
                               (sprawdz(self.p_brakrozdzialu), użytkownik))
            sprawdz(self.p_brakrozdzialu)

            connection.execute('UPDATE FORMULARZE SET ROZDZIALY=? WHERE USERNAME=?;',
                               (sprawdz(self.p_rozdzialy), użytkownik))
            sprawdz(self.p_rozdzialy)

            connection.execute('UPDATE FORMULARZE SET GLOWNYKOBIETA=? WHERE USERNAME=?;',
                               (sprawdz(self.p_glownybohaterkobieta), użytkownik))
            sprawdz(self.p_glownybohaterkobieta)

            connection.execute('UPDATE FORMULARZE SET GLOWNYMEZCZYZNA=? WHERE USERNAME=?;',
                               (sprawdz(self.p_glownybohatermezczyzna), użytkownik))
            sprawdz(self.p_glownybohatermezczyzna)

            connection.execute('UPDATE FORMULARZE SET NARRATOR1=? WHERE USERNAME=?;',
                               (sprawdz(self.p_narrator1), użytkownik))
            sprawdz(self.p_narrator1)

            connection.execute('UPDATE FORMULARZE SET NARRATOR3=? WHERE USERNAME=?;',
                               (sprawdz(self.p_narrator3), użytkownik))
            sprawdz(self.p_narrator3)

            connection.execute('UPDATE FORMULARZE SET PAUTOR=? WHERE USERNAME=?;',
                               (sprawdz(self.p_polskiautor), użytkownik))
            sprawdz(self.p_polskiautor)

            connection.execute('UPDATE FORMULARZE SET ZAUTOR=? WHERE USERNAME=?;',
                               (sprawdz(self.p_zagranicznyautor), użytkownik))
            sprawdz(self.p_zagranicznyautor)

            connection.execute('UPDATE FORMULARZE SET CZASPRZESZLOSC=? WHERE USERNAME=?;',
                               (sprawdz(self.p_przeszlosc), użytkownik))
            sprawdz(self.p_przeszlosc)

            connection.execute('UPDATE FORMULARZE SET CZASPRZYSZLOSC=? WHERE USERNAME=?;',
                               (sprawdz(self.p_przyszlosc), użytkownik))
            sprawdz(self.p_przyszlosc)

            connection.execute('UPDATE FORMULARZE SET CZASTERAZ=? WHERE USERNAME=?;',
                               (sprawdz(self.p_terazniejszosc), użytkownik))
            sprawdz(self.p_terazniejszosc)

            connection.execute('UPDATE FORMULARZE SET TFANTASTYCZNA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_fantastyczna), użytkownik))
            sprawdz(self.t_fantastyczna)

            connection.execute('UPDATE FORMULARZE SET TFANTASTYCZNONAUKOWA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_fantastycznonaukowa), użytkownik))
            sprawdz(self.t_fantastycznonaukowa)

            connection.execute('UPDATE FORMULARZE SET TGOTYCKA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_gotycka), użytkownik))
            sprawdz(self.t_gotycka)

            connection.execute('UPDATE FORMULARZE SET THISTORYCZNA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_historyczna), użytkownik))
            sprawdz(self.t_historyczna)

            connection.execute('UPDATE FORMULARZE SET TKRYMINALNA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_kryminalna), użytkownik))
            sprawdz(self.t_kryminalna)

            connection.execute('UPDATE FORMULARZE SET TLOTRZYSKOWSKA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_lotrzyskowska), użytkownik))
            sprawdz(self.t_lotrzyskowska)

            connection.execute('UPDATE FORMULARZE SET TMARYNISTYCZNA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_marynistyczna), użytkownik))
            sprawdz(self.t_marynistyczna)

            connection.execute('UPDATE FORMULARZE SET TPRODUKCYJNA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_produkcyjna), użytkownik))
            sprawdz(self.t_produkcyjna)

            connection.execute('UPDATE FORMULARZE SET TPRZYGODOWA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_przygodowa), użytkownik))
            sprawdz(self.t_przygodowa)

            connection.execute('UPDATE FORMULARZE SET TPSYCHOLOGICZNA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_psychologiczna), użytkownik))
            sprawdz(self.t_psychologiczna)

            connection.execute('UPDATE FORMULARZE SET TSENSACYJNA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_sensacyjna), użytkownik))
            sprawdz(self.t_sensacyjna)

            connection.execute('UPDATE FORMULARZE SET TSENTYMENTALNA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_sentymentalna), użytkownik))
            sprawdz(self.t_sentymentalna)

            connection.execute('UPDATE FORMULARZE SET TSPOLECZNOOBYCZAJOWA=? WHERE USERNAME=?;',
                               (sprawdz(self.t_spolecznoobyczajowa), użytkownik))
            sprawdz(self.t_spolecznoobyczajowa)

            connection.execute('UPDATE FORMULARZE SET AUTOR=? WHERE USERNAME=?;',
                               (self.ulubionyautor.currentText(), użytkownik))


            connection.execute('UPDATE FORMULARZE SET WIEK=? WHERE USERNAME=?;',
                               (self.wiek.currentText(), użytkownik))


            connection.execute('UPDATE FORMULARZE SET ILOSCSTRON=? WHERE USERNAME=?;',
                               (self.iloscstron.currentText(), użytkownik))

            connection.execute('UPDATE FORMULARZE SET JEZYK=? WHERE USERNAME=?;',
                               (self.jezykksiazki.currentText(), użytkownik))
            try:
                if self.b_wwieku.isChecked()==True:
                    connection.execute('UPDATE FORMULARZE SET BWIEKU=? WHERE USERNAME=?;',
                                       ('2', użytkownik))
                elif self.b_wwieku.isChecked()==False:
                    connection.execute('UPDATE FORMULARZE SET BWIEKU=? WHERE USERNAME=?;',
                                       ('0', użytkownik))
                if self.b_mlodszy.isChecked()==True:
                    connection.execute('UPDATE FORMULARZE SET BMLODSZY=? WHERE USERNAME=?;',
                                       ('2', użytkownik))
                elif self.b_mlodszy.isChecked()==False:
                    connection.execute('UPDATE FORMULARZE SET BMLODSZY=? WHERE USERNAME=?;',
                                       ('0', użytkownik))
                if self.b_starszy.isChecked()==True:
                    connection.execute('UPDATE FORMULARZE SET BSTARSZY=? WHERE USERNAME=?;',
                                       ('2', użytkownik))
                elif self.b_starszy.isChecked()== False:
                    connection.execute('UPDATE FORMULARZE SET BSTARSZY=? WHERE USERNAME=?;',
                                       ('0', użytkownik))
                if self.b_obojetnie.isChecked()==True:
                    connection.execute('UPDATE FORMULARZE SET BOBOJETNIE=? WHERE USERNAME=?;',
                                       ('2', użytkownik))
                elif self.b_obojetnie.isChecked()==False:
                    connection.execute('UPDATE FORMULARZE SET BOBOJETNIE=? WHERE USERNAME=?;',
                                       ('0', użytkownik))

            except:
                print('cos nie tak')
            connection.commit()
            connection.close()

        def dodajliste():
            con1 = sqlite3.connect("books.db")
            con2 = sqlite3.connect("formularze.db")
            con3 = sqlite3.connect("login.db")
            listaużytkownika = []
            zalogowany = con3.execute('SELECT * FROM USERS WHERE ZALOGOWANY=1')
            for osoba in zalogowany:
                użytkownik = osoba[0]

            result2 = con2.execute("SELECT * FROM FORMULARZE")

            result1 = con1.execute("SELECT * FROM BOOKS")
            listazwiekiem=[]
            listazilosciastron=[]
            for data2 in result2:
                if data2[0] == użytkownik:
                    for data in result1:
                        #########################wyswietla wiecej ksiazek im wiecej rzeczy się zaznaczy#################
                        #for i in range(0, 33, 1):
                         #   if data[i] == data2[i]:
                          #      if data[i] != 0:
                           #         listaużytkownika.append(data[0])
                        ################## zeby zawsze  wyswietlalo wszystkie pozycje ulubionego autora#################
                        if data[1] == data2[1]:
                                listaużytkownika.append(data[0])
                        ################# wyswietlanie ksiazek w ktorych nie ma podziału ze względu na wiek ############
                        #print('tutaj: ',data[-2])
                        if data[-2] == 0:
                            listazwiekiem.append(data[0])
                            #print(data[2])
                        ############################starszy#############################################################
                        if data2[-4]==2:
                            if data2[-6]<data[-2]:
                                listazwiekiem.append(data[0])
                        ###########################mlodszy##############################################################
                        if data2[-3]==2:
                            if data2[-6]>data[-2]:
                                listazwiekiem.append(data[0])
                        ##########################w tym samym wieku ####################################################
                        if data2[-1]==2:
                            if data2[-6]==data[-2]:
                                listazwiekiem.append(data[0])
                        ###########################obojetnie ###########################################################
                        if data2[-2]==2:
                                listazwiekiem.append(data[0])
                        ####################################sprawdzanie zaznaczonej liczby stron #######################
                        #print(data[17])
                        if data2[17]=="0-100":
                            if data[17]==1:
                                listazilosciastron.append(data[0])
                                #print('1 przedział')
                        if data2[17] =="100-500":
                            if data[17] == 2:
                                listazilosciastron.append(data[0])
                                #print('2 przedział')
                        if data2[17] =="500-inf":
                            if data[17] == 3:
                                listazilosciastron.append(data[0])
                                #print('3 przedział')


                        #####################im wiecej wynikow tym wezsze poszukiwania##################################
                        for i in range(3,32,1):
                            if i != 17 and i !=18: ######## z pominieciem wynikow ktore nigdy nie sa puste##############
                                if data2[i]!=0:
                                    czyzgodne=1
                                    if data2[i] != data[i]:
                                        czyzgodne=0

                        if czyzgodne==1:
                            listaużytkownika.append(data[0])
            ##################### porównuje wybrany wiek autora i ilosc stron###########################################
            listazwiekiem=set(listazwiekiem).intersection(set(listazilosciastron))
            listaużytkownika=(set(listazwiekiem).intersection(set(listaużytkownika)))
            #print(listaużytkownika)
            con2.execute("UPDATE FORMULARZE SET TITLE=(?) WHERE USERNAME=(?);", (str(listaużytkownika), użytkownik))

            con1.commit()
            con2.commit()
            con3.commit()
            con1.close()
            con2.close()
            con3.close()
            Youbook.hide()
        def zamnijokno():
            Youbook.hide()

        Youbook.setObjectName("Youbook")
        Youbook.resize(784, 598)
        Youbook.setMinimumSize(QtCore.QSize(784, 598))
        Youbook.setMaximumSize(QtCore.QSize(784, 598))
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
        for i in range(0, 101, 1):
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
        self.Cancel.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.01 rgba(255, 112, 112, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Cancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.Cancel.setObjectName("Cancel")

        self.Cancel.accepted.connect(sprawdzwszystkie)
        self.Cancel.accepted.connect(dodajliste)
        self.Cancel.rejected.connect(zamnijokno)


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

        ################# liczba miejsc na języki ######################################################################
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
        ###############################################################################################################

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
        ###################### liczba miejsc na autorow ################################################################
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
        ################################################################################################################

        self.ulubionyautor.setItemText(64, "")
        self.horizontalLayout_5.addWidget(self.ulubionyautor)
        self.jakiuzytkownik = QtWidgets.QLabel(self.centralwidget)
        self.jakiuzytkownik.setGeometry(QtCore.QRect(580, 0, 191, 41))
        self.jakiuzytkownik.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.01 rgba(255, 112, 112, 255), stop:1 rgba(255, 255, 255, 255));")
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
        for i in range(0, 101, 1):
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
        i = 1
        lista = []
        for data in result:
            lista.append(data)
        lista = list(set(lista))
        for data in lista:
            self.ulubionyautor.setItemText(i, _translate("Youbook", data[0]))
            i = i + 1
        connection.commit()
        connection.close()
        #####################################################################################
        con = sqlite3.connect("login.db")
        zalogowany = con.execute('SELECT * FROM USERS WHERE ZALOGOWANY=1')
        for osoba in zalogowany:
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


class Ui_Youbook2(object):
    def zmienokno(self):
        self.Youbook = QtWidgets.QMainWindow()
        self.ui = Ui_Youbook()
        self.ui.setupUi(self.Youbook)
        self.Youbook.show()


    def openYoubook3(self):
        self.Youbook3 = QtWidgets.QMainWindow()
        self.ui     = Ui_Youbook3()
        self.ui.setupUi(self.Youbook3)
        self.Youbook3.show()

    def setupUi(self, Youbook2):
        Youbook2.setObjectName("Youbook2")
        Youbook2.resize(784, 598)
        Youbook2.setMinimumSize(QtCore.QSize(784, 598))
        Youbook2.setMaximumSize(QtCore.QSize(784, 598))
        Youbook2.setSizeIncrement(QtCore.QSize(5, 2))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        Youbook2.setFont(font)
        Youbook2.setStyleSheet("background-color: rgb(248, 120, 120);\n"
                               "selection-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Youbook2)
        self.centralwidget.setObjectName("centralwidget")
        self.jakiuzytkownik = QtWidgets.QLabel(self.centralwidget)
        self.jakiuzytkownik.setGeometry(QtCore.QRect(580, 0, 191, 41))
        self.jakiuzytkownik.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.01 rgba(255, 112, 112, 255), stop:1 rgba(255, 255, 255, 255));")
        self.jakiuzytkownik.setObjectName("jakiuzytkownik")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 500, 761, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(362, 16777215))
        self.pushButton_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.01 rgba(255, 112, 112, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_2.clicked.connect(self.zmienokno)

        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setSizeIncrement(QtCore.QSize(0, 3))
        self.pushButton.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.01 rgba(255, 112, 112, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton.clicked.connect(self.openYoubook3)


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 110, 761, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.01 rgba(255, 112, 112, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 180, 761, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 759, 309))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 741, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        Youbook2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Youbook2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 784, 21))
        self.menubar.setObjectName("menubar")
        self.menuWype_nij_formularz = QtWidgets.QMenu(self.menubar)
        self.menuWype_nij_formularz.setObjectName("menuWype_nij_formularz")
        self.menuFormularz = QtWidgets.QMenu(self.menuWype_nij_formularz)
        self.menuFormularz.setObjectName("menuFormularz")
        Youbook2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Youbook2)
        self.statusbar.setObjectName("statusbar")
        Youbook2.setStatusBar(self.statusbar)
        self.Twojalista = QtWidgets.QAction(Youbook2)
        self.Twojalista.setObjectName("Twojalista")

        self.Twojalista.triggered.connect(self.openYoubook3)

        self.Wyloguj = QtWidgets.QAction(Youbook2)
        self.Wyloguj.setObjectName("Wyloguj")
        self.Nowy = QtWidgets.QAction(Youbook2)
        self.Nowy.setObjectName("Nowy")
        self.Popraw = QtWidgets.QAction(Youbook2)
        self.Popraw.setObjectName("Popraw")
        self.Zamknij = QtWidgets.QAction(Youbook2)
        self.Zamknij.setObjectName("Zamknij")
        self.menuFormularz.addAction(self.Nowy)




        self.menuFormularz.addAction(self.Popraw)
        self.menuWype_nij_formularz.addAction(self.menuFormularz.menuAction())
        self.menuWype_nij_formularz.addAction(self.Twojalista)
        self.menuWype_nij_formularz.addSeparator()
        self.menuWype_nij_formularz.addAction(self.Wyloguj)
        self.menuWype_nij_formularz.addAction(self.Zamknij)
        self.menubar.addAction(self.menuWype_nij_formularz.menuAction())

        self.retranslateUi(Youbook2)
        QtCore.QMetaObject.connectSlotsByName(Youbook2)

    def retranslateUi(self, Youbook2):
        _translate = QtCore.QCoreApplication.translate
        Youbook2.setWindowTitle(_translate("Youbook2", "BOOK&YOU"))

        #####################################################################################
        time.sleep(1)
        con = sqlite3.connect("login.db")
        zalogowany = con.execute('SELECT * FROM USERS WHERE ZALOGOWANY=1')
        for osoba in zalogowany:
            użytkownik = osoba[0]
        con.commit()
        con.close()
        nazwa_użytkownika = "Użytkownik : " + str(użytkownik)

        self.jakiuzytkownik.setText(_translate("Youbook2", nazwa_użytkownika))
        self.pushButton_2.setText(_translate("Youbook2", "Nowy Formularz"))
        self.pushButton.setText(_translate("Youbook2", "Moja lista"))
        self.label.setText(_translate("Youbook2",
                                      "Witaj ! BOOK&YOU to aplikacja, która pomoże Ci znaleźć książki napisane specjalnie dla Ciebie!"))
        self.label_3.setText(_translate("Youbook2", "Instrucja obsługi !"))
        self.label_4.setText(_translate("Youbook2", "1.Wypełnij formularz, im więcej informacji podasz tym bardziej precyzyjne będą poszukiwania\n "))
        self.label_5.setText(_translate("Youbook2", "2.Jeżeli chcesz zobaczyć listę swoich książek wejdz w ikone 'Moja Lista' na ekranie\n "
                                                    "wyswietli się wtedy lista związana z Twoim ostatnim formularzem "))
        self.label_6.setText(_translate("Youbook2", "3.Jeżeli chcesz wyszukac nowe książki wypełnij nowy formularz, przeczytane pozycje nie będą sie pojawiały w propozycjach"))
        self.label_2.setText(_translate("Youbook2", "4.Aby zaznaczyć że jakieś książki juz przeczytałeś/aś zaznacz pozycję na liście i kliknij 'Zapisz zmiany', zmiany będą widoczne po ponownym otworzeniu listy"))
        self.menuWype_nij_formularz.setTitle(_translate("Youbook2", "Menu"))
        self.menuFormularz.setTitle(_translate("Youbook2", "Fomularz"))
        self.Twojalista.setText(_translate("Youbook2", "Twoja lista"))
        self.Wyloguj.setText(_translate("Youbook2", "Wyloguj"))
        self.Nowy.setText(_translate("Youbook2", "Nowy formularz"))
        self.Popraw.setText(_translate("Youbook2", "Popraw swój formularz"))
        self.Zamknij.setText(_translate("Youbook2", "Zamknij"))


if __name__ == "__main__":
    ui = Ui_Youbook2()
    nazwa = 'Youbook2'
    import sys

    app = QtWidgets.QApplication(sys.argv)
    nazwa = QtWidgets.QMainWindow()
    ui.setupUi(nazwa)
    nazwa.show()
    sys.exit(app.exec_())



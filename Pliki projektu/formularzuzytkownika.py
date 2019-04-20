import sqlite3

def  createTable():
    connection = sqlite3.connect("formularze.db")
    conlogin = sqlite3.connect("login.db")
    resultlogin = conlogin.execute("SELECT USERNAME FROM USERS")

    connection.execute("CREATE TABLE IF NOT EXISTS FORMULARZE(USERNAME TEXT,"
                       "AUTOR TEXT,"
                       "TITLE TEXT,"
                       "REAL INTEGER,"
                       "FANTASTIC INTEGER,"
                       "FACTS INTEGER,"
                       "NARRATOR1 INTEGER,"
                       "NARRATOR3 INTEGER,"
                       "PAUTOR INTEGER,"
                       "ZAUTOR INTEGER,"
                       "GLOWNYKOBIETA INTEGER,"
                       "GLOWNYMEZCZYZNA INTEGER,"
                       "CZASTERAZ INTEGER,"
                       "CZASPRZYSZLOSC INTEGER,"
                       "CZASPRZESZLOSC INTEGER,"
                       "ROZDZIALY INTEGER,"
                       "BRAKROZDZIALY INTEGER,"
                       "ILOSCSTRON INTEGER,"
                       "JEZYK TEXT,"
                       "TFANTASTYCZNA INTEGER,"
                       "TFANTASTYCZNONAUKOWA INTEGER,"
                       "TGOTYCKA INTEGER,"
                       "THISTORYCZNA INTEGER,"
                       "TKRYMINALNA INTEGER,"
                       "TLOTRZYSKOWSKA INTEGER,"
                       "TMARYNISTYCZNA INTEGER,"
                       "TPRODUKCYJNA INTEGER,"
                       "TPRZYGODOWA INTEGER,"
                       "TPSYCHOLOGICZNA INTEGER,"
                       "TSENSACYJNA INTEGER,"
                       "TSENTYMENTALNA INTEGER,"
                       "TSPOLECZNOOBYCZAJOWA INTEGER"
                       "WIEKB INTEGER)")

    #czyścimy baze użytkowników
    #connection.execute('DELETE FROM USERS')


    #wrzucamy wszystkich użytkowników do bazy
    #for login in resultlogin:
    #    connection.execute('INSERT INTO FORMULARZE(USERNAME) VALUES(?);', (login))




    connection.commit()
    conlogin.commit()
    result = connection.execute("SELECT * FROM FORMULARZE")

    for data in result:
        print(data[0])


    connection.close()
    conlogin.close()
createTable()

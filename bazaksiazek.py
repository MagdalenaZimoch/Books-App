import sqlite3

def  createTable():
    connection = sqlite3.connect("books.db")

    connection.execute("CREATE TABLE IF NOT EXISTS BOOKS(id INTEGER PRIMARY KEY ASC,"
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

    connection.commit()

    result = connection.execute("SELECT * FROM BOOKS")

    for data in result:
        print("Uniwersalny kod : ", data[0])
        print(data[1]," - ",data[2])




    connection.close()
createTable()
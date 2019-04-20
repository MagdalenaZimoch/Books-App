import sqlite3

def  createTable():
    connection = sqlite3.connect("login.db")

    connection.execute("CREATE TABLE IF NOT EXISTS USERS(USERNAME TEXT NOT NULL,EMAIL TEXT,PASSWORD TEXT) ")
    #czyścimy baze użytkowników
    #connection.execute('DELETE FROM USERS')

    connection.commit()

    result = connection.execute("SELECT * FROM USERS")

    for data in result:
        print("Login : ", data[0])
        print("Adres E-mail : ", data[1])
        print("Hasło : ",data[2])

    connection.close()
createTable()

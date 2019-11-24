import sqlite3


def create_user(username,password): #username and password is arguments
    db = sqlite3.connect("db.sqlite", isolation_level=None)

    db.cursor().execute(
        "INSERT INTO Users(Username, PWHash)" 
        "VALUES(?, ?)", (username, password), #varibles gets added in order
    )

#Quarying it
def get_data():
    db = sqlite3.connect("db.sqlite", isolation_level=None)

    rows = db.cursor().execute(
        "SELECT * " #Selecting the column "*" means all
        "   FROM Users" #Name of Table being selected
    )

#Showing rows in database
    for row in rows:
        print(row)

#Adding Data Not needed
'''def add_data():
    db = sqlite3.connect("db.sqlite", isolation_level=None)

    db.cursor().execute(
        "INSERT INTO Users(Username, PWHash)"
        "VALUES('userID', 'passwordID')"
    )'''

#Creating Tables
def tables():
        db = sqlite3.connect("db.sqlite", isolation_level=None)


#Creating Data Tables
        db.cursor().execute(
            "CREATE TABLE IF NOT EXISTS Users("
            "   ID INTEGER PRIMARY KEY AUTOINCREMENT,"
            "   PWHash varchar,"
            "   Username varchar(255)"
        ");"
        )


#calling functions
tables()
#add_data()
get_data()

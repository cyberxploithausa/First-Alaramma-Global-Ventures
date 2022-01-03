import sqlite3

#Creating the database
def clientsData():
    conn = sqlite3.connect("client.db")
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS client (id INTEGER PRIMARY KEY, CustID TEXT, Firstname TEXT, Surname TEXT, DoB TEXT, \
            Gender TEXT, Address TEXT, Mobile1 INTEGER  )"
    )
    conn.commit()
    conn.close()


def addRec(CustID, Firstname, Surname, DoB, Gender, Address, Mobile1):
    conn = sqlite3.connect("client.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO client VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)", (CustID, Firstname, Surname, DoB, Gender, Address, Mobile1)
    )
    conn.commit()
    conn.close()

def viewRec():
    conn = sqlite3.connect("client.db")
    c = conn.cursor()
    c.execute(
        "SELECT * FROM client"
    )
    row = c.fetchall()
    conn.commit()
    conn.close()
    return row


def updateRec(id, CustID="", Firstname="", Surname="", DoB="", Gender="", Address="", Mobile1=""):
    conn = sqlite3.connect("client.db")
    c = conn.cursor()
    c.execute(
        "UPDATE client SET CustID= ?, Firstname= ?, Surname= ?, DoB= ?, Gender= ?, Address=?, Mobile1= ? \
            WHERE id=?", (CustID, Firstname, Surname, DoB, Gender, Address, Mobile1, id)
    )
    conn.commit()
    conn.close()

def searchRec(CustID="", Firstname="", Surname="", DoB="", Gender="", Address="", Mobile1=""):
    conn = sqlite3.connect("client.db")
    c = conn.cursor()
    c.execute(
        "SELECT * FROM client WHERE CustID=? OR Firstname=? OR Surname=? OR DoB=? OR Gender=? OR Address=? \
            OR Mobile1=? ", (CustID, Firstname, Surname, DoB, Gender, Address, Mobile1)
    )
    row = c.fetchall()
    conn.commit()
    conn.close()
    return row

def deleteRec(id):
    conn = sqlite3.connect("client.db")
    c = conn.cursor()
    c.execute(
        "DELETE FROM client WHERE id=?", (id,)
    )
    conn.commit()
    conn.close()

clientsData()
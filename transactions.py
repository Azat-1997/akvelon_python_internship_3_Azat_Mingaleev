import sqlite3
import datetime
sqlite3.enable_callback_tracebacks(True)
 
connection = sqlite3.connect("transaction.db")
cursor = connection.cursor()
# create table of users if this one not exists
 
cursor.execute(""" CREATE TABLE IF NOT EXISTS users (userID INT PRIMARY KEY,
 firstname TEXT NOT NULL,
 lastname TEXT NOT NULL,
 email TEXT); """)
 
cursor.execute(""" CREATE TABLE IF NOT EXISTS trans (transID INT PRIMARY KEY,
 amount REAL,
 date INT,
 userID INT NOT NULL,
 FOREIGN KEY (userID) REFERENCES users(userID)); """)

connection.commit()
 

def add_user(connection, firstname:str, lastname:str, email:str):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (firstname, lastname, email) VALUES (?, ?, ?);", (firstname, lastname, email))
    connection.commit()
 
        
def add_transaction(connection, user_id: int, amount:str, date:str):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO trans (user_id, amount, date) VALUES (?, ?, ?);", (user_id, amount, date))
    connection.commit()
    
def update_user(connection, id:int, firstname:str, lastname, email):
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET firstname = ?, lastname = ?, email = ?, WHERE userID = ? ;", (firstname, lastname, email, id))
    connection.commit()   


def update_transaction(connection, id, user_id, amount, date):
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET userID = ?, amount = ?, date = ?, WHERE transID = ?;", (user_id, amount, date, id))
    connection.commit()

    
def remove_user(connection, id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?;", (id,))
    connection.commit()

def remove_transaction(connection, id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM trans WHERE id = ?;", (id,))
    connection.commit()




add_user(connection, )

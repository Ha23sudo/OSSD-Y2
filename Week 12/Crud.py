import sqlite3

def create_database():
    
        
    conn=sqlite3.connect('app.db')

    cursor=conn.cursor()

    create_table=''' CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER   
    )
    '''

    cursor.execute(create_table)

    conn.commit()
    conn.close()


def add_user():
    conn=sqlite3.connect('app.db')
    cursor=conn.cursor()
    insert='INSERT INTO users(name,age) VALUES(?,?)'
    cursor.execute(insert, ("Ali", 23))
    conn.commit()
    conn.close()














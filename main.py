import sqlite3
import os
import json

def practica1():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE users (dni text, nombre text, altura real)")
    cur.execute("INSERT INTO users VALUES ('X', 'isaac', '1.85')")
    con.commit()
    con.close()





    os.remove("database.db")


if __name__ == '__main__':
    practica1()


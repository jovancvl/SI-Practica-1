import sqlite3

def practica1():
    con = sqlite3.connect('example.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE usuario (dni text, nombre text, altura real)")
    cur.execute("INSERT INTO usuario VALUES ('X', 'isaac', '1.85')")
    con.commit()
    con.close()


if __name__ == '__main__':
    practica1()


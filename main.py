import sqlite3
import os
import json

def practica1():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS usuarios (name TEXT, telefono INTEGER, contrasena TEXT, provincia TEXT, permisos TEXT)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS emails (name TEXT, total INTEGER, phishing INTEGER, cliclados INTEGER)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS fechas (name TEXT, value TEXT)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS ips (name TEXT, value TEXT)")
    con.commit()
    source = json.loads(open("users.json").read())
    users = source['usuarios'] # is list

    #print(users[0].keys())
    #name = list(users[0].keys())[0]
    #print(users[0][name]["telefono"])

    for u in users:
        name = list(u.keys())[0] # is string
        values = u[name] # is dict
        cur.execute("INSERT INTO usuarios VALUES (?, ?, ?, ?, ?)", (name, values["telefono"], values["contrasena"], values["provincia"], values["permisos"]))
        e = values["emails"]
        cur.execute("INSERT INTO emails VALUES (?, ?, ?, ?)", (name, e["total"], e["phishing"], e["cliclados"]))
        for f in values["fechas"]:
            cur.execute("INSERT INTO fechas VALUES (?, ?)", (name, f))
        for ip in values["ips"]:
            cur.execute("INSERT INTO ips VALUES (?, ?)", (name, ip))
        con.commit()

    #cur.execute('drop table if exists usuarios')
    #con.commit()
    con.close()



if __name__ == '__main__':
    practica1()


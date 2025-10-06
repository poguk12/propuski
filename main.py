from datetime import date
import sqlite3

propuski_list = {}

dt_now = date.today().strftime('%Y-%m-%d')


def BD(prichina, namePrepod):

    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
    
        query = """INSERT INTO propuski (Date, Prichina, Prepod) VALUES(?, ?, ?)"""
        values = (dt_now, prichina, namePrepod)

        cursor.execute(query, values)

        cursor.execute("SELECT * FROM propuski")

        db.commit()

def Vivod():
 with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM propuski")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

rodik = True

while rodik:
    prichina = input("Введите причину пропуска: ")
    teacher = input("Введите имя или предмет пропуска: ")

    if prichina == "1":
         Vivod()
    else:
        BD(prichina, teacher)
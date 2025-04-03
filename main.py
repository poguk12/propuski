from datetime import date
import sqlite3

list = {

}

dt_now = date.today()

db = sqlite3.connect('propusk.db')
cursor = db.cursor()

#cursor.execute("""
#CREATE TABLE propuski (
#    Date text,
#    Prichina text,
#    Prepod text
#)""")

#cursor.execute("INSERT INTO propuski VALUES ('date', 'prichina', 'teacher')")

cursor.execute("SELECT rowid, * FROM propuski WHERE rowid > 2")

items = cursor.fetchall()

for el in items:
    print(el[1] + " - " + el[3])

db.commit()

db.close()

def add_propusk(date, prichina, teacher):

    if date in list:
        list[date].append(prichina  + " " + teacher)
    else:
        list[date] = []
        list[date].append(prichina + " " + teacher)

    print("Пропуск ", prichina, " добавлена на дату ", date)

rodik = True

while rodik:

    slovo = input("Введите задание: ")

    if "add" == slovo :
        date = input("Введите дату пропуска: ")
        prichina = input("Введите причину пропуска: ")
        teacher = input("Введите имя или предмет пропуска: ")

        if date == "Сегодня" :
            date = dt_now

        add_propusk(date, prichina, teacher)

    elif "show" == slovo:
        date = input("Введите дату для отображения списка задач: ")

        if date in list:
            print("На дату", date, " есть несколько пропусков: ")
            for task in list[date]:
                print('- ', task)
        else:
            print("Нет задач на эту дату")

    elif "exit" == slovo:
        rodik = False




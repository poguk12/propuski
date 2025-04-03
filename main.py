from datetime import date

list = {

}

dt_now = date.today()

print(dt_now)


def add_propusk(date, prichina, teacher):

    if list.get(dt_now) is not None:
        list[date].append(prichina)
    else:
        list[date] = [prichina + " " + teacher]


while True:

    slovo = input("Введите задание: ")

    if("add" == slovo):
        date = input("Введите дату пропуска: ")
        prichina = input("Введите причину пропуска: ")
        teacher = input("Введите имя или предмет пропуска: ")

        if(date == "Seg"):
            date = dt_now

        add_propusk(date, prichina, teacher)

    elif ("show" == slovo):
        print(list)




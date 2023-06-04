"""
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные.
2. Программа должна сохранять данные в текстовом файле.
3. Пользователь может ввести одну из характеристик для поиска определенной записи.
4. Пользователь может изменить и удалить данные.
5. Использование функций: программа не должна быть линейной.
"""

def writedown_person():
    lastname = input("Фамилия: ")
    name = input("Имя: ")
    middlename = input("Отчество: ")
    tel = input("Телефон: ")
    data = open("phonebook.txt", "a", encoding = "utf-8")
    data.write(f"{lastname}---{name}---{middlename}---{tel} \n")
    data.close()

def search_person():
    parameter = input("Введите параметр поиска: ")
    search_bool = False
    with open("phonebook.txt", "r", encoding = "utf-8") as data:
        for line in data:
            if parameter in line:
                print(line)
                search_bool = True
        if search_bool == False:
            print("Такой записи нет")

def print_phonebook():
    with open("phonebook.txt", "r", encoding = "utf-8") as data:
        for line in data:
            print(line)

def load_path():
    new_phonebook = input("Введите путь нового справочника: ")
    with open("phonebook.txt", "r+", encoding="utf-8") as data:
        with open(new_phonebook, "r", encoding = "utf-8") as new_data:
            for line in new_data:
                if line not in data:
                    data.write(line)

def change_data():
    changeable_line = input("Введите параметр записи, которую необходимо изменить: ")
    with open("phonebook.txt", "r", encoding = "utf-8") as data:
        lines = data.readlines()
        with open("phonebook.txt", "w", encoding = "utf-8") as new_data:
            for line in lines:
                if changeable_line not in line:
                    new_data.write(line)
                else:
                    ask = input("Укажите, что конкретно необходимо изменить (1 - фамилия, 2 - имя, 3 - отчество, 4 - телефон): ")
                    while ask not in ('1', '2', '3', '4'):
                        print("Введен параметр, которого нет в справочнике")
                        ask = input("Укажите, что конкретно необходимо изменить (1 - фамилия, 2 - имя, 3 - отчество, 4 - телефон): ")
                    new_parameter = input("Введите новые данные: ")
                    line_list = line.split("---")
                    line_list[int(ask) - 1] = new_parameter
                    new_data.write("---".join(line_list))

def delete_line():
    removable_line = input("Введите параметр записи, которую необходимо удалить: ")
    with open("phonebook.txt", "r", encoding = "utf-8") as data:
        lines = data.readlines()
        with open("phonebook.txt", "w", encoding = "utf-8") as new_data:
            for line in lines:
                if removable_line not in line:
                    new_data.write(line)
                else:
                    print(line)
                    ask = input("Необходимо удалить данную запись (да/нет)?: ")
                    while ask not in ("да", "нет"):
                        print("Введен некорректный ответ")
                        ask = input("Необходимо удалить данную запись (да/нет)?: ")
                    if ask == "нет":
                        new_data.write(line)

print("""1 - добавление персоны в справочник,
2 - поиск персоны в справочнике,
3 - вывод на экран всего справочника,
4 - импорт данных в справочник из другого справочника,
5 - изменение данных в записи справочника,
6 - удаление записи из справочника""")

request = int(input("Введите номер запроса: "))
if request == 1:
    writedown_person()
elif request == 2:
    search_person()
elif request == 3:
    print_phonebook()
elif request == 4:
    load_path()
elif request == 5:
    change_data()
elif request == 6:
    delete_line()
else:
    print("Такого запроса нет")

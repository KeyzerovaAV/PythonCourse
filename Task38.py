"""
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные.
2. Программа должна сохранять данные в текстовом файле.
3. Пользователь может ввести одну из характеристик для поиска определенной записи.
4. Использование функций: программа не должна быть линейной.
"""

def writedown_person():
    lastname = input("Фамилия: ")
    name = input("Имя: ")
    middlename = input("Отчество: ")
    tel = input("Телефон: ")
    data = open("phonebook.txt", "a", encoding = "utf-8")
    data.write(f"Фамилия: {lastname} -- Имя: {name} -- Отчество: {middlename} -- Телефон: {tel} \n")
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
    with open(new_phonebook, "r", encoding = "utf-8") as new_data:
        with open("phonebook.txt", "a+", encoding="utf-8") as data:
            for line in new_data:
                if line not in data:
                    data.write(line)

print("""1 - добавление персоны в справочник,
2 - поиск персоны в справочнике,
3 - вывод на экран всего справочника,
4 - импорт в справочник из другого справочника""")

request = int(input("Введите номер запроса: "))
if request == 1:
    writedown_person()
elif request == 2:
    search_person()
elif request == 3:
    print_phonebook()
elif request == 4:
    load_path()
else:
    print("Такого запроса нет")

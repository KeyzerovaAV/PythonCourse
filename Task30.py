"""
Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.
"""

def get_arithmetic_progression(element_1, step, elements_count):
    arithmetic_progression = [element_1 + i * step for i in range(elements_count)]
    return arithmetic_progression

first_element = int(input("Введите первый элемент арифметической прогрессии: "))
difference = int(input("Введите разность между элементами арифметической прогрессии: "))
number_of_elements = int(input("Введите количество элементов арифметической прогрессии: "))

print(*get_arithmetic_progression(first_element, difference, number_of_elements))

"""
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума).
"""

def get_index_list(array, minimum, maximum):
    index_list = []
    for i in range(len(array)):
        if maximum >= array[i] >= minimum:
            index_list.append(i)
    return index_list

my_array = [int(i) for i in input().split()]
min_element = int(input("Введите минимальный элемент диапазона: "))
max_element = int(input("Введите максимальный элемент диапазона: "))

print(*get_index_list(my_array, min_element, max_element))

"""
Дан массив, состоящий из целых чисел. Написать программу, которая в данном массиве определяет 
количество элементов, у которых два соседних, и при этом оба соседних элемента, меньше данного. 
Сначала вводится число N — количество элементов в массиве. Далее записаны N чисел — элементы массива. 
Массив состоит из целых чисел.
"""

from random import randint

def get_array(array_len):
    return [randint(1, 10) for _ in range(array_len)]

my_array_len = int(input("Введите количество элементов массива: "))
my_array = get_array(my_array_len)
print(*my_array)

counter = 0
for i in range(1, my_array_len - 1):
    if my_array[i - 1] < my_array[i] > my_array[i + 1]:
        counter += 1
print(counter)

"""
Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), 
которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, 
затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива.
"""

from random import randint

def get_array(array_len):
    array = [randint(1, 50) for _ in range(array_len)]
    return array

def find_unique_numbers(array1, array2):
    for i in range(array1_len):
        if array1[i] not in array2:
            print(array1[i], end = ' ')

array1_len = int(input("Введите количество элементов первого массива: "))
my_array1 = get_array(array1_len)
array2_len = int(input("Введите количество элементов второго массива: "))
my_array2 = get_array(array2_len)

print(*my_array1)
print(*my_array2)
find_unique_numbers(my_array1, my_array2)

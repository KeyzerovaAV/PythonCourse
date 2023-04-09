"""
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
"""

from random import randint
n = int(input("Введите число N - количество элементов в массиве: "))
list_1 = [randint(1, 10) for _ in range(n)]
x = randint(1, 10)
print(*list_1)
print(x)

nearest_values_set = set()
nearest_value = list_1[0]
min_difference = abs(x - list_1[0])
for i in range(n):
    current_difference = abs(x - list_1[i])
    if current_difference < min_difference:
        min_difference = current_difference
        nearest_value = list_1[i]
        nearest_values_set.clear()
        nearest_values_set.add(nearest_value)
    elif current_difference == min_difference:
        nearest_values_set.add(list_1[i])

print(f"Самые близкие по величине элементы к числу {x}:")
print(*nearest_values_set)

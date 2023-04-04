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

nearest_value_set = set()
nearest_value = list_1[0]
min_difference = abs(x - list_1[0])
if min_difference == 0:
    min_difference += 1

for number in list_1:
    current_difference = abs(x - number)
    if current_difference < min_difference and current_difference != 0:
        min_difference = current_difference
        nearest_value = number
        nearest_value_set.clear()
        nearest_value_set.add(nearest_value)
    elif current_difference == min_difference and current_difference != 0:
        nearest_value_set.add(number)

print(f"Самые близкие (но не равные) по величине элементы к числу {x}:")
print(*nearest_value_set)

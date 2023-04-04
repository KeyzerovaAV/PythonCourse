"""
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
"""

from random import randint
n = int(input("Введите число N - количество элементов в массиве: "))
list_1 = [randint(1, n) for _ in range(n)]
x = list_1[randint(0, n - 1)]
print(*list_1)
print(x)

counter = 0
for i in range(n):
    if list_1[i] == x:
        counter += 1
print(counter)

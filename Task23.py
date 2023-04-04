"""
Дан массив, состоящий из целых чисел. Напишите программу, 
которая подсчитает количество элементов массива, больших предыдущего 
(элемента с предыдущим номером).
"""

from random import randint
n = int(input("Введите количество элементов массива: "))
list_1 = [randint(-10, 10) for _ in range(n)]
print(list_1)

counter = 0
for i in range(1, n):
    if list_1[i - 1] < list_1[i]:
        counter += 1
print(counter)

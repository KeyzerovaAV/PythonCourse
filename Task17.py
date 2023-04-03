"""
Дан список чисел. Определите, сколько в нем встречается различных чисел. 
Пользователь может вводить значения списка или список задан изначально.
"""

from random import randint

list = []
n = int(input("Введите количество элементов в списке: "))
for i in range(n):
    list.append(randint(-5, 5))
print(list)
print(len(set(list)))

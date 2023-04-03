"""
Дан список чисел. Определите, сколько в нем встречается различных чисел. 
Пользователь может вводить значения списка или список задан изначально.
"""

from random import randint

list_1 = []
n = int(input("Введите количество элементов в списке: "))
for i in range(n):
    list_1.append(randint(-5, 5))
print(list_1)
print(len(set(list_1)))

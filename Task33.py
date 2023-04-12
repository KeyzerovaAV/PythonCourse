"""
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
Написать программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
"""

from random import randint
def marks(n):
    array = [randint(1, 5) for _ in range(n)]
    print(array)
    return(array)

def maxmin(array):
    large = max(array)
    small = min(array)
    for i in range(len(array)):
        if array[i] == large:
            array[i] = small
    return array

magazine = marks(10)
print(maxmin(magazine))

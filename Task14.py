"""
Требуется вывести все целые степени двойки, не превосходящие числа N.
"""

number = int(input("Введите число N: "))
power = 1
while power <= number:
    print(power, end = "  ")
    power *= 2

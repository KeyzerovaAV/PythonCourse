"""
Написать программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
"""

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

def raise_to_power(a, b):
    if b == 0:
        return 1
    return a * raise_to_power(a, b - 1)

print(raise_to_power(a, b))

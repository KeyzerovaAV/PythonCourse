"""
По данному целому неотрицательному числу n вычислите значение n!. N! = 1 * 2 * 3 * … * N 
(произведение всех чисел от 1 до N) 0! = 1. Решить задачу, используя цикл while.
"""

N = int(input("Введите неотрицательное число N: "))

if N >= 0:
    number = 1
    factorial = 1
    while number <= N:
        factorial *= number
        number += 1
    print(f"{N}! = {factorial}")
else:
    print(f"Ошибка: число {N} - отрицательное.")

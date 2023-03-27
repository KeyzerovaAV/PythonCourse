"""
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
то есть выведите такое число n, что φ(n) = A. Если A не является числом Фибоначчи, выведите число -1.
"""

a = int(input("Введите число a, которое больше 1: "))
if a > 1:
    previousNumber = 0
    currentNumber = 1
    count = 2
    while currentNumber < a:
        previousNumber, currentNumber = currentNumber, previousNumber + currentNumber
        count += 1
    if currentNumber == a:
        print(count)
    else:
        print(-1)
else:
    print(f"Ошибка: число {a} не больше 1")

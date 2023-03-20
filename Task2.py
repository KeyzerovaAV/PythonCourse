"""
Найдите сумму цифр трехзначного числа.
"""

n = int(input('Введите трехзначное число: '))

if n >= 100 and n <= 999:
    digit1 = n // 100
    digit2 = n // 10 % 10
    digit3 = n % 10
    sum = digit1 + digit2 + digit3
    print(f"Сумма цифр числа {n} = {sum}")
else:
    print(f"Ошибка: число {n} не трехзначное")

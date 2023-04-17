"""
Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n 
(включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. 
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
Программа получает на вход одно натуральное число k, не превосходящее 10 в 5-й степени. 
Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. 
Пары необходимо выводить по одной в строке, разделяя пробелами. 
Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
"""

def get_divisor_sum(n):
    total_sum = 0
    for i in range(1, int(n ** 0.5 + 1)):
        if n % i == 0:
            total_sum += i + n // i
    return total_sum - n

k = int(input("Введите число не больше 10 в 5-й степени: "))
unique = []
for first_number in range(1, k + 1):
    if first_number not in unique:
        second_number = get_divisor_sum(first_number)
    if get_divisor_sum(second_number) == first_number and first_number != second_number:
        print(first_number, second_number)
        unique.append(second_number)

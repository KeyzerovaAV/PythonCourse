"""
Пользователь вводит число N (1 <= N <= 100). Далее построчно выводятся рандомно N целых чисел в диапазоне от -50 до 50. 
Нужно вывести наибольшее количество идущих подряд положительных чисел.
"""

n = int(input("Введите количество дней периода наблюдения за температурой: "))
count_current = 0
count_max = 0
for i in range(n):
    temperature = int(input("Введите среднесуточную температуру: "))
    if temperature > 0:
        count_current += 1
    elif count_current != 0:
        if count_current > count_max:
            count_max = count_current
        count_current = 0
if count_current > count_max:
    count_max = count_current
print("Наибольшее количество идущих подряд дней с положительной температурой за период наблюдения =", count_max)

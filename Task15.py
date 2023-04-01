"""
Пользователь вводит одно число N - количество арбузов. Далее идут N чисел, записанных на новой строке каждое.
Каждое число - это масса соответствующего арбуза. Вывести максимальную и минимальную массу, используя циклы.
"""

from random import randint

number_of_watermelons = int(input("Введите количество арбузов: "))
maximum_weight = randint(1, 50)
print(maximum_weight)
minimum_weight = maximum_weight
for i in range(number_of_watermelons - 1):
    weight = randint(1, 50)
    print(weight)
    if weight > maximum_weight:
        maximum_weight = weight
    elif weight < minimum_weight:
        minimum_weight = weight
print(f"Самый тяжелый арбуз весит {maximum_weight} кг, а самый легкий арбуз весит {minimum_weight} кг")

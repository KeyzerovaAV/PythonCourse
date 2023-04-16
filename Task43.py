"""
Дан список чисел. Посчитать, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу, образуют одну пару, которую необходимо посчитать. 
Вводится список чисел. Все числа списка находятся на разных строках.
"""

my_array = [int(i) for i in input().split()]

total_counter = 0
for i in range(len(my_array) - 1):
    current_counter = my_array[i + 1:].count(my_array[i])
    total_counter += current_counter
print(total_counter)

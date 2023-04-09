"""
Напишите программу, которая принимает на вход строку и отслеживает, 
сколько раз каждый символ уже встречался. Количество повторов добавляется к символам 
с помощью постфикса формата _n. Для решения данной задачи используйте функцию .split()
"""

text = "a a a b c a a d c d d".split()
new_dict = {}
result = ""
for i in text:
    if i in new_dict:
        result += i + "_" + str(new_dict[i]) + " "
        new_dict[i] += 1
    else:
        new_dict[i] = 1
        result += i + " "
print(result)

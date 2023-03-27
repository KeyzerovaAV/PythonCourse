"""
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).
"""

n = int(input("Введите число долек шоколадки по одной стороне: "))
m = int(input("Введите число долек шоколадки по другой стороне: "))
k = int(input("Введите число долек шоколадки, которые можно отломить за один разлом по прямой: "))

if k < (n * m) and (k % n == 0 or k % m == 0):
    print('yes')
else:
    print('no')
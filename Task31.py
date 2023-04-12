"""
Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где 
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется через рекурсию найти N-е число Фибоначчи.
"""

n = int(input("Введите число N: "))
def fibonacci(n):
    if n == 1:
        return 0
    elif n in [2, 3]:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(n))

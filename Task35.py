"""
Написать функцию, которая принимает одно число и проверяет, является ли оно простым.
Простое число - это число, которое имеет только 2 делителя: 1 и n (само число).
"""

def check_simple_number(n):
    if n == 1:
        return "no"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "no"
    return "yes"
print(check_simple_number(int(input("Enter a number: "))))

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4
def Sum(A, B):
    A += 1
    if B == 1:
        return A
    return Sum(A, B - 1)

A = int(input("введите число A: "))
B = int(input("введите число B: "))
print(Sum(A, B))

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*
# 2 2
#     4 

ferst_number = int(input("Введите первое чилсло: "))
second_number = int(input("Введите второе число: "))
def rec_sum(ferst_number, second_number):
    if second_number == 0:
        return ferst_number
    return rec_sum(ferst_number+1, second_number-1)
print(rec_sum(ferst_number, second_number))
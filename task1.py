# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


number = int(input("Введите число: "))
degree = int(input("Введите его степень: "))

def exponentiation(number, degree):
    if (degree == 1):
        return (number)
    if (degree != 1):
        return (number * exponentiation(number, degree - 1))

print("Результат возведения в степень равен:", exponentiation(number, degree))
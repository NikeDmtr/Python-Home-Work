#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# num = int(input('Введите число дня недели от 1 до 7 - '))
# if num < 1 or num > 7:
#     print('Вы ввели не верное число')
# elif num > 5:
#     print(f'{num} -> Да')
# else:
#     print(f'{num} -> Нет')



# 2.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# result = True
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             print(f'{x = } {y = } {z = }  {not(x or y or z) == (not x and not y and not z)}')
# 3.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


# x=int(input('Введите координату - x: '))
# y=int(input('Введите координату - y: '))
#
# if  x > 0 and y > 0:
#     print(f'Точка ({x}, {y}) -> 1-я ось')
# elif x < 0 and y > 0:
#     print(f'Точка ({x}, {y}) -> 2-я ось')
# elif x < 0 and y < 0:
#     print(f'Точка ({x}, {y}) -> 3-я ось')
# elif x > 0 and y < 0:
#     print(f'Точка ({x}, {y}) -> 4-я ось')


# 4.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# a = int(input('введите номер координатной четверти: '))
# if a == 1:
#     print("х от 0 до +∞, у от 0 до +∞")
# elif a == 2:
#     print("х от 0 до -∞, у от 0 до +∞")
# elif a == 3:
#     print("х от 0 до-∞, у от 0 до -∞")
# elif a == 4:
#     print("х от 0 до +∞, у от 0 до -∞")
# else:
#     print("Такого числа нету!!!!!!")





# 5.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


# x1 = int(input('Введите координату х1: '))
# y1 = int(input('Введите координату y1: '))
# x2 = int(input('Введите координату х2: '))
# y2 = int(input('Введите координату y2: '))
# import math
# sqrt = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2),2)
# print(f'(A - ({x1}, {y1})  B - ({x2}, {y2}) = {sqrt}')
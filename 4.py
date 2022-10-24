# Разбор домашки
# Из десятичной в двоичную
# a = 14
# st = ''
# while a > 0:
#     ost = a % 2 # выдаёт остаток числа а
#     st = str(ost) + st
#     a = a // 2 # деление на 2
# print(st)    

# a = 14
# print(bin(a)[2:])# Перевод в десятичную систему с исп. среза([2:]), где 2 с какого символа,: по какой
                   #если пустое поле, то до конца

#рекурсия для Фибоначи:
# def fib(n):
#     if n ==1:
#         return 1
#     elif n == 0:
#         return 0
#     else:
#         return fib(n - 1) + fib(n - 2)

# for i in range(10):
#     print(fib(i))                 

#1. Задайте строку из набора чисел
# # def input_number():
# lst = []
# lst = list(map(int, input('Введите числа через пробел ').split()))

#Напишите программу которая покажет наименьшее и наибольшее число
# print(max(lst))
# print(min(lst))
# def maximum_minimum_number_lst(lst):
#     i_Max = lst[0]
#     i_Min = lst[0]
# for i in range(1, len(lst)):
#     if lst[i] > i_Max:
#         i_Max = lst[i]
#     if lst[i] < i_Min:
#         i_Min = lst[i]
#         print(f'Максимальное число: {i_Max}')
#         print(f'Минимальное число: {i_Min}')

# 2. Найдите корни квадратного уровнения Ax2 + Bx+C = 0 двумя способами
#    1. С помощью математических формул нахождения корней квадратного уровнения
#    2. С помощью дополнительных библиотек Python
# def quadratic_equation(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if d < 0:
#         print('действительных корней нет')
#     elif d ==0:
#         res =-b / (2 *a)
#         print([res])
#     else:
#         res1 = (-b + d ** 0.5) / (2 * a)
#         res2 = (-b - d ** 0.5) / (2 * a)
#         print([res1, res2])
# def quadratic_equation_sympy(a, b, c):
#     x = sympy.Symbol('x')
#     n = sympy.solve(a * x ** 2 + b *x + c, x)     
#     print(n)   


# 3. Задайте два числа. Напишите программу которая найдёт НОК
# (наименьшее общее кратное) этих двух чисел.

# num_1 = int(input('Введите число: '))
# num_2 = int(input('Введите число: '))
# i = min(num_1, num_2)
# while True:
#     if i % num_1 == 0 and i % num_2 == 0:
#         break
#     i += 1
# print(i)    

# Домашнее задание

# Вычислить число Пи c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# import math
# x = 0
# y = 0
# for t in range(1,10000001):
#     if t % 2 != 0:
#         y += 1
#         if y % 2 != 0:
#             x += 1/t
#         else:
#             x -= 1/t
#     else:
#         pass
# print(toFixed((x*4), 3)) 

# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

# import math 
# def prime_factors(N): 
#     while N % 2 == 0: 
#         print(2, end = ' ') 
#         N = N / 2 
#     for i in range(3, int(math.sqrt(N)) + 1, 2): 
#          while N % i == 0: 
#             print(i, end = ' ') 
#             N = N / i 
#     if N > 2: 
#         print(N) 
# N = int(input('Введите число: ')) 
# prime_factors(N)



# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.

#numbers = [20, 20, 30, 30, 40]
# lst = []
# for i in numbers:
#     n = 0
#     for x in numbers:
#         if i == x:
#             n += 1
#     if n == 1:
#         lst.append(i)
# print(lst)                
# # 2 Вариант
# from random import random
# data = []
# for i in range(10):
#     data.append(int(random()*10))
# print(data)

# lst = []
# for i in data:
#     if data.count(i) == 1:# выявляет колличество элементов в списке
#         lst.append(i)
# print(lst)        

# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
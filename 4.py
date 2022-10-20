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
# print(max(nums))
# print(min(nums))
# # def maximum_minimum_number_lst(lst):
# i_max = lst[0]
# i_min = lst[0]
# for i in range(1, len(lst)):
#     if lst[i] > i_max:
#         i_max = lst[i]
#     if lst[i] < i_min:
#         i_min = lst[i]
#         print(f'Максимальное число: {i_max}')
#         print(f'Минимальное число: {i_min}')

# 2. Найдите корни квадратного уровнения Ax2 + Bx+C = 0 двумя способами
#    1. С помощью математических формул нахождения корней квадратного уровнения
#    2. С помощью дополнительных библиотек Python
def quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('действительных корней нет')
    elif d ==0:
        res =-b / (2 *a)
        print([res])
    else:
        res1 = (-b + d ** 0.5) / (2 * a)
        res2 = (-b - d ** 0.5) / (2 * a)
        print([res1, res2])
def quadratic_equation_sympy(a, b, c):
    x = sympy.Symbol('x')
    n = sympy.solve(a * x ** 2 + b *x + c, x)     
    print(n)   
#2



# 3. Задайте два числа. Напишите программу которая найдёт НОК
# (наименьшее общее кратное) этих двух чисел.


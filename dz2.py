import math
# Напишите программу, которая принимает на вход вещественное число и показывает
# сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
#-------------------------------------------------------------------------------------------
# num = input('Введите вещественное число: ')
# amound = 0
# num1 = num.replace('.','')
# for i in num1:
#    amound += int(i)
# print('Сумма цифр равна: ' + str(amound))
#--------------------------------------------------------------------------------------------



# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#--------------------------------------------------------------------------------------------

# n = int(input('Введите целое число: '))
#
# for i in range(1, n):
#     print(math.factorial(i), end=', ')
# print(math.factorial(n))
#--------------------------------------------------------------------------------------------




# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
#--------------------------------------------------------------------------------------------
# n = int(input('введите число: '))
# amount = 0
# for i in range(1, n+1):
#     amount += ((1 + (1/i)) ** i)
# print(amount)



#--------------------------------------------------------------------------------------------


# *4. НЕОБЯЗАТЕЛЬНАЯ ЗАДАЧА
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на
# указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
#
# Реализуйте алгоритм перемешивания списка.

#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#
# ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)

list1 = [1, 2, 3, 2, 0]
list2 = [5, 1, 2, 7, 3, 2]
result = []

for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            result.append(list1[i])
            break
print(result)
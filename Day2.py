

# num=int(input('Введите число: '))
# for i in range(num):
#     print((-3)**i, end=', ')




# 2. Для натурального n создать словарь индекс - значение, состоящий
#    из элементов последовательности 3 n + 1.
# *Пример: *
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


# n = int(input('введите число:'))
# for i in range(1, n):
#    print(f'{i}: {3 * i + 1}', end=', ')
#    print(f'{i+1}:{3} * i+ 2}')
#
#
# number = int(input('Введите число: '))
# print('{',end='')
# for i in range(1, number + 1):
#     if i != number:
#         print(f'{i}: {3 * i + 1}', end=', ')
#     else:
#         print(f'{i}: {3 * i + 1}', end='')
# print('}')
#



# 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

# str1 = (input('введите первую строку:'))
# str2 = (input('введите вторую строку:'))
#
# for i in range(str1)


# from random import randint
# a = []
# for i in range(10):
#     a.append(randint(0, 10))
# print(a)
#
# from random import randint
# b = []
# for i in range(10):
#     b.append(randint(0, 10))
# print(b)
#
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
#             break
# print(c)


string_input = input('Введите текст: ')
string_elevent = input('Введите элемент: ')
print(string_input.count(string_elevent))


n = int(input())
a = []
for i in range(n):
    a.append((-3) ** i)
print(*a, sep=', ')



# n = int(input())
# print('{', end='')
# for i in range(1, n):
#     print(f'{i}:{3 * i + 1}', end=', ')
# print(f'{n}:{3 * n + 1}', end='}')


# some_str_1 = input()
# some_str_2 = input()
# len_str_2 = len(some_str_2)
# i = 0
# count = 0
# while i < len(some_str_1):
#     if some_str_1[i:i + len_str_2] == some_str_2:
#         count += 1
#     i += 1
# print(count)

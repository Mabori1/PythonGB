# number = int(input())
# maxx = number
# for _ in range(4):
#     number = int(input())
#     if number > maxx:
#         maxx = number
# print(maxx)
#
# some_list = []
# for _ in range(5):
#     number = int(input())
#     some_list.append(number)
# maxx = some_list[0]
# for element in some_list:
#     if element > maxx:
#         maxx = element
# print(maxx)

print(max(map(int, input().split())))


# number = int(input())
# maxx = number
# for _ in range(4):
#     number = int(input())
#     if number > maxx:
#         maxx = number
# print(maxx)
#
# some_list = []
# for _ in range(5):
#     number = int(input())
#     some_list.append(number)
# maxx = some_list[0]
# for element in some_list:
#     if element > maxx:
#         maxx = element
# print(maxx)

#print(max(map(int, input().split())))

# n = int(input())
# for i in range(-n, n):
#     print(i, end=', ')
# print(n)

# print(list(range(-n, n + 1)), sep=', ')

# Напишите программу, которая будет на вход принимать число N и выводит числа от - N до N


# number = int(input())
# for i in range(-number, number + 1):
#     print(i, end= " ")

# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# number1 = input('input number: ')
# if '.' not in number1:
#     print('no')
# else:
#     num = (float(number1) * 10) % 10
#     print(int(num))
# n = input()

# if '.' in n:
#     index_t = n.find('.')
#     print(n[index_t + 1])
# else:
#     print('нет')

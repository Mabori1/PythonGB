# Напишите программу, удаляющую из текста все слова, содержащие "абв".

# txt = input("Введите текст через пробел:\n")
# print(f"Исходный текст: {txt}")
# find_txt = "абв"
# lst = [i for i in txt.split() if find_txt not in i]
# print(f'Результат: {" ".join(lst)}')
# --------------------------------------------------------------------------

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая
# ход друг после друга. Первый ход определяется жеребьёвкой. За один ход
# можно забрать не более чем 28 конфет. Все конфеты оппонента достаются
# сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#
# from random import randint
#
# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x
#
# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")
#
# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
#
# counter1 = 0
# counter2 = 0
#
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)
#
# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")
# --------------------------------------------------------------------------

# Реализовать RLE алгоритм.реализовать модуль сжатия и восстановления
# данных.  Входные и выходные данные хранятся в отдельных файлах


with open('dz5_RLE1_decoded.txt', 'r') as data:
    my_text = data.read()


def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code


str_code = encode_rle(my_text)
print(str_code)


with open('dz5_RLE2_encoded.txt', 'r') as data:
    my_text2 = data.read()


def decoding_rle(ss: str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode


str_decode = decoding_rle(my_text2)
print(str_decode)
# --------------------------------------------------------------------------

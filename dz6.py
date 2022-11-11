
# ================================================================================
input_array = ['в', '5', 'часов', '17', 'минут',
               'температура', 'воздуха', 'была', '+5', 'градусов']

for _ in range(len(input_array)):

    element = input_array.pop(0)

    if element.isdigit():
        input_array.append(f'"{int(element):02d}"')

    elif element[0] == "+" and element[1].isdigit():
        input_array.append(f'"+{int(element):02d}"')

    else:
        input_array.append(element)

print(' '.join(input_array))


# ================================================================================

input_array = ['инженер-конструктор Игорь',
               'главный бухгалтер МАРИНА',
               'токарь высшего разряда нИКОЛАй',
               'директор аэлита']

for string in input_array:
    good_name = string.split()[-1].capitalize()
    print(f"Привет, {good_name}!")
# ================================================================================

input_array = [57.8, 46.51, 97, 22.14, 33.42, 39.33, 89.43, 29.66, 38.01, 14.00,
               0.22, 1, 67, 23.99, 99.99, 73.01]

print(input_array)

print(f"{'a':-^79}")

end_word: str = ", "

for i, num in enumerate(input_array):

    fix_price = str(f"{float(num):.2f}").split(".")

    if i == len(input_array) - 1:
        end_word = "\n"

    print(f"{fix_price[0]} руб {fix_price[1]} коп", end=end_word)

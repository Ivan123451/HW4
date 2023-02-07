# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#
# string = 'aaaaaaasssssddddaa'
# new_str = '7a5s4d2a'

string = input('введите набор букв:')

string_new = string + '.'

my_list = list(string_new)

# print(my_list)
new_str = str()
my_counts = 1
for i in range(1, len(my_list)):
    if my_list[i] == my_list[i-1]:
        my_counts += 1
    elif my_list[i] != my_list[i-1]:
        new_str += f'{my_counts}{my_list[i-1]}'
        my_counts = 1

print(f'первое преобразование: {new_str}')

new_list = list(new_str)

# print(new_list)

numbers_list = []
letters_list = []

for i in range(len(new_list)):
    if i % 2 == 0:
        numbers_list.append(new_list[i])
    elif i % 2 == 1:
        letters_list.append(new_list[i])

# print(numbers_list)
# print(letters_list)

summa = 0
for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])
    summa += numbers_list[i]
# print(numbers_list)

final_str = str()

for i in range(len(numbers_list)):
    final_str += numbers_list[i]*letters_list[i]

print(f'обратное преобразование: {final_str}')





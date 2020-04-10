# number_list = [1, 2, 3, 5, 10, 12]
# for num in number_list:
#     print(num)
#     print('Hola')
#     print(str(num) + 'Hola')
#     # print('Hi')

# for num in number_list:
#   if num % 2 == 0:
#     print(num)
#   else:
#     print('Hey!')
# number_list = [1, 2, 3, 4, 5, 10]
#
# list_number_sum = 0
#
# for num in number_list:
#
#     list_number_sum = list_number_sum + num
#
#     print(list_number_sum)# вывод в теле цикла
# print(list_number_sum) # вывод за пределами цикла

# greeting = 'Hello Python'
# for letter in greeting:
#     for letter in 'Hello Python':
    # print(letter)
    # if letter =='o':
    #     print(letter)

# for letter in 'Hello Python':
#         if letter != 'o':
#            print(letter)

# for letter in 'Hello Python':
#     print('One more letter')

# tuple list
# tuple_list_1 = [('a', 'b'), ('c', 'd'), ('e', 'f')]
# for item in tuple_list_1:
#     print (item)
# for letter_1, letter_2 in tuple_list_1:
#     print(letter_1, letter_2)
#     print(letter_1)
#     print(letter_2)

# tuple_list_1 = [('a', 'b', 1), ('c', 'd', 5), ('e', 'f', 7)]
# for letter_1, letter_2, number in tuple_list_1:
#     print(letter_1, letter_2, number)

# dictionary

# dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
#key-value pairs in tuple
# for item in dictionary.items():
#         print(item)
#keys
# for item in dictionary:
#     print(item)
# for item in dictionary.keys():
#     print(item)
# for item in dictionary.items():
#         print(item)
# for item in dictionary.values():
#     print(item)
# for key, value in dictionary.items():
#         print(key)




# пример от kiber
# sum = 0
# numbers = [20,100,10]
# for num in numbers:
#     print('Before', sum)
# sum += num
# print('After', sum)
# print('Result', sum)

# for x in range(5):
#     print(x)
#     print("Hello!")
#     for _ in range(5):
#         print(x)
#     print("Hello!")

#Задание от Юрия

# 1. Используйте цикл for для вычисления суммы всех чётных
# чисел в диапазоне от 10 до 30 (включая крайние значения). Выведите результат на печать

diap_chet = 0
for diap in range(9, 31):
    if diap % 2 == 0:
        diap_chet = diap_chet + diap
print(diap_chet)

#Получите от пользователя число на вводе и
# используйте цикл for для вывода на экран текста
# 'Hello!' столько же раз

user_input = input('введите целое число:')
for enter in user_input:
 print('Hello!' * int(enter))


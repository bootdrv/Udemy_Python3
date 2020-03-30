rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'}
print(rainbow_colors)
print(type(rainbow_colors))

# emty_set = {} # данная строка с пустым значением относится к классу dictionary
emty_set = set() # данная строка с пустым значением относится к классу set
print(emty_set)
print(type(emty_set))

number_list = [3, 2, 5, 45, 1, 1, 1, 5, 45]
text_tuple = ('adsasd', 'werwer', 'qwe', 'qweqwe', 'werwer', 'werwer', 'werwer', 'adsasd')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)
#  добавляем значенния и строки
set_from_list.add(765)
set_from_tuple.add('Hello')
# одинаковые значения не дублируются при выводе изза уникальности, а эти уже есть
set_from_list.add(765)
set_from_tuple.add('Hello')
# удаляем элемент из множества
set_from_list.pop()    # удаляет случайное значение но его возвращает
set_from_list.remove(3)  # удаляет заданное значение,
set_from_list.discard(45)
# set_from_list.remove(3) если этого элемента уже нет - выдастся ошибка
set_from_list.discard(3)  # если этого элемента уже нет - ошибка не выдастся. запрос проигнорится
# set_from_list.clear()   # очистка множества
# set_from_tuple.clear()   # очистка множества
print(set_from_list)
print(set_from_tuple)
# Множества- это не упорядоченная структура!!!!

# Задание от Юрия
main_list = [70, 2, 45, 4, 30, 1]
# main_tuple = ('red', 'white', 'purple')
set_main = set(main_list)
# set_tuple =(main_tuple)
print(set_main)
# print(set_tuple)

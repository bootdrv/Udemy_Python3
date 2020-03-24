# tuple - это кортеж(похож на список(list) но он не изменяемый(immutable)
# tuple_1 = (1, 2, 3) # скобки желательно использовать всегда в tuple
# tuple_2 = ('one', 'hello')
# tuple_3 = (3, 4.65, 'tree')
# tuple_4 = 1, 2, 3 # скобки все равно добавятся автоматом при выводе
# # tuple_1[1] = 3 эта команда работать не будет, т.к нельзя изменить текщее значение
# #Но мы можем создать новый кортеж и присваивая старые значения менять элементы по индексам
# new_tuple = (tuple_1[0], 3, tuple_1[2])
# print(tuple_1)
# print(tuple_2)
# print(tuple_3)
# print(tuple_4)
# print(tuple_1 [1]) # вывод по индексу
# print(new_tuple)
# # tuple  используется в основном для того чтобы случайно не изменились данные в кортеже
# # в этом его отличие от list
person_tuple = ('John', 'Smith', 1974)
# Raspakovka dannih v tuple
#Prisvaivaniye znacheniy
x = y = z = 12
addon = x, y, z = 12, 13, 14
print(x, y, z)
# создаем переменную для извлечения данных и присваиваем person_tuple
first_name, last_name, year_of_birth = person_tuple
# выводим на экран все значения переменных
print(first_name, last_name, year_of_birth)
t1 = (1, 2, 3, 4, 5, 7, 9, 1 )
# вызываем в  tuple метод count - он возвращает количество элементов
print(t1.count(5))
print(t1.count(1))
greetings_tuple = ('hello', 'hi', 'hey', 'hi')
print(greetings_tuple.count('hi'))
print(greetings_tuple.count('hello'))
print(greetings_tuple.count('hodo'))
#vichisliayem index
print(t1.index(5))
print(greetings_tuple.index('hi')) # вычисляем индекс повторяющихся значений
# -выведется индекс первого значения из всех повторяющихся- ближайшего из одинаковых


# zadaniye ot yuriya
# Создайте объект tuple, описывающий компьютер и распакуйте его в
# соответствующие переменные. Выведите переменные вызвав функцию print() один раз
pc_tuple = (
    #komjplektuha
    'case: logic-power',
    'Mb: Asus',
    'cpu: intel Core i7',
    'ram: kingston ddr 4 8Gb',
    'video: Geforce 9900',
    'hdd: tochiba 1TB',
    'dvd: lg dvd-ram black',
    'monitor: samsung 23',
    'keyb: logitech 104 k',
    'mouse: a4tech 3b')
case, mb, cpu, ram, video_card, hdd, dvd_rw, monitor, keyb, mouse = pc_tuple
print('\n'.join (pc_tuple)) #выводим каждое значение с новой строки в столбик


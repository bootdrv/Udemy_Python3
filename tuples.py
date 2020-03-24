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
# sozdayem peremennuyu dlia izvlecheniya dannih i prisvaivayem  person_tuple
first_name, last_name, year_of_birth = person_tuple
# vivodim na ekran vse znacheniya peremennih
print(first_name, last_name, year_of_birth)
t1 = (1, 2, 3, 4, 5, 7, 9, 1 )
# vizivayem v tuple metod count - on vozvraschayet kolichestvo elementov
print(t1.count(5))
print(t1.count(1))
greetings_tuple = ('hello', 'hi', 'hey', 'hi')
print(greetings_tuple.count('hi'))
print(greetings_tuple.count('hello'))
print(greetings_tuple.count('hodo'))
#vichisliayem index
print(t1.index(5))
print(greetings_tuple.index('hi')) # vichislit index povtoriayuschihsia znacheniy
# -vivedet index pervogo znacheniya- blijayshego iz odinakovix





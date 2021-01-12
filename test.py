print(2 + 2)
print(2 - 2)
print(2 * 2)
print(2 / 2)
print(2 // 2)
print(3 // 2)
print(2 ** 3)
print(5 % 3)

# next

x = 5
print(x)
x = 'hello'
print(x)

# next
greeting = 'hello'
print(greeting)
first_name = "Jack"
last_name = 'White'
print(greeting + first_name + last_name)
long_string = 'this is Loooong string'
print(long_string)
# Escaping
some_string = 'I\'m a programmer'
print(some_string)
another_string = "I want to learn \"Python\""
print(another_string)
another_string = 'I want to learn "Python"'
print(another_string)
string_w_new_line = "hello \nMy name is Kostya"
print(string_w_new_line)
numbers = '1\t23\t4567'
print(numbers)
some_text = "\thello! \n\tI'm very glad too see you!"
print(some_text)

# tripple quots

string_tipple = """This is ' text with "triple quotes" """
print(string_tipple)
string_second = '''This is ' text with "triple quotes" '''
print(string_second)

# Indexing & Slicing
# Indexing
greeting = 'Hello Python!'
greeting_lenght = len(greeting)
print(greeting_lenght)
print(greeting[0])
print(greeting[-1])
print(greeting[12])
print(greeting[-4])
# Slicing
print(greeting[2:5])
print(greeting[6:10])
print(greeting[-5:-2])
print(greeting[6:10])
print(greeting[5:])
print(greeting[:7])
print(greeting[:])
print(greeting[::2])
print(greeting[::1])
print(greeting[::3])
print(greeting[1::3])
print(greeting[1:9:3])
print(greeting[::-1])

# Strinh_Formatting

# print(1 + 1)
# print('1' + '1')
# age = 23
# print('Lack is' + age + 'years old/') так неправильно конкатенировать-строки с числами
# print('Lack is ' + str(age) + ' years old')
# print('Lack is ' + str(23) + ' years old')

# name = 'Jack'
# age = 23
# name_and_age ='My name is {0}. I\'m {1} years old.'.format(name, age)
# print(name_and_age)
# name_and_age ='My name is {0}. I\'m {1} years old.'.format('Jack', 23)
# print(name_and_age)
# name_and_age ='My name is {}. I\'m {} years old.'.format('Jack', 23)
# print(name_and_age)
# name_and_age ='My name is {}. I\'m {} years old.'.format(23,'Jack')
# print(name_and_age)
# week_days = 'There are 7 days in a week: {}, {}, {}, {}, {}, {}, {}.'\
#     .format('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
# print(week_days)
# week_days = 'There are 7 days in a week: {6}, {0}, {1}, {3}, {2}, {4}, {5}.' \
#     .format('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
# print(week_days)
# week_days = 'There are 7 days in a week: {su}, {mo}, {tu}, {th}, {we}, {fr}, {sa}.' \
#     .format(mo = 'Monday', tu = 'Tuesday', we= 'Wednesday', th = 'Thursday', fr = 'Friday', sa = 'Saturday', su = 'Sunday' )
# print(week_days)

# float_result = 1000/ 7
# print(float_result)
# print('The result of division is {0}'.format(float_result))
# print('The result of division is {0:1.3f}'.format(float_result))
# print('''
# {}{}{}
# {}{}{}
# {}{}{}
# '''.format(1.4445, 346.23232332, 34.5656, 1234.23,
#            1.456777, 345.232323, 34.2344, 1234.23,
#            456.23233))
# float_result = 1000/ 7
# print(float_result)
# print('The result of division is {0}'.format(float_result))
# print('The result of division is {0:1.3f}'.format(float_result))
# print('''
# {} {} {}
# {} {} {}
# {} {} {}
# '''.format(1.4445, 346.23232332, 34.5656, 1234.23,
#            1.456777, 345.232323, 34.2344, 1234.23,
#            456.23233))
# float_result = 1000/ 7
# print(float_result)
# print('The result of division is {0}'.format(float_result))
# print('The result of division is {0:1.3f}'.format(float_result))
# print('''
# {0:10.2f} {1:10.2f} {2:10.2f}
# {3:10.2f} {4:10.2f} {5:10.2f}
# {6:10.2f} {7:10.2f} {8:10.2f}
# '''.format(1.4445, 346.23232332, 34.5656, 1234.23,
#            1.456777, 345.232323, 34.2344, 1234.23,
#            456.23233))

name = 'Jack'
age = 23
name_and_age ='My name is {0}. I\'m {1} years old.'.format(name, age)
print(name_and_age)
name_and_age = f'My name is {name}. I\'m {age} years old.'
print(name_and_age)
print('My name is %s. %s %d years old' % (name, "I'm", age)) # python 2.7  в 3 не рекомендовано юзать

# Lists
number_list = (32, 21, 47, 34.15)
print(number_list)
some_list = (12, 35.334, 'hello')
print(some_list)
print(len(some_list))



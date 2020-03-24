# car_prices = {'opel':5000, 'honda': 8000, 'BMW': 1000}
# print(car_prices)
# print(car_prices['BMW'])
# car_prices['mazda'] = 4000
# print(car_prices)
# # change  opel price
# car_prices['opel'] = 2000
# print(car_prices)
# # del  item honda
# del car_prices['honda']
# print(car_prices)
# # delete all item car_prices
# # del car_prices - ne vkliucat!!!
# # clear all item car_prices
# car_prices.clear()
# print(car_prices)
person = {
    'first name': 'Kostiantyn',
    'last name': 'Drv',
    'age': "47",
    'Hobbies': ['fishing', 'cinema', 'IT'],
    'children': {'son': 'Yuriy', 'daughter': 'Kristina'}
}
print(person['age'])
print(person['Hobbies'])
hobbies = person['Hobbies']
# izvlekayem opredelionniye dannie
print(hobbies[2])
print(person['Hobbies'] [2])
children = person['children']
print(children)
print(children['son'])
print(person['children']['son'])
# ADD ITEMS
person['car'] = 'shevrolet'
# change hobbies item on 0 position
person['Hobbies'] [0] = 'basketbool'
# add new hobbies
new_hobby = hobbies.append([3, 'new_hobbies'])
person['Hobbies'] [3] = 'new_hobbies'
print(person)
print(person.keys())
print(person.values())
print(person.items())

#zadaniye ot yuriya
dictionary = {'mb': 85, 'cpu': 180, 'ram': 8, 'hdd': 50}
print("cpu:",dictionary['cpu'])

dictionary ={
    # PC components
    'Case': 'Mini-tower w power-supply cheftec 600w',
    'complectuha': ['Motherboard', 'Cpu', 'Ram', 'hdd','videocard', 'dvd_rw'],
    'input_outpud_dev': ['Monitor', 'keyboard', 'mouse'],
    'multimedia': ['Speakers', 'webcam']
    }
print(dictionary)

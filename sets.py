'''
dic = {
        'name': 'rinat',
        'age': 18,
        'sex': 'male'
}
#print(dic)
#dic.clear()

print(dic.get('name'))

print(dic.keys())
print(dic.values())

print(dic.items())

f = {'zp': 50000}
dic.update({'surname': 'azamatov'})
dic.update(f)
print(dic)



set = {121, 2121}
print(type(set))
ls = list(set)
print(type(ls))
'''
'''
dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
print(dates_of_birth)
dates_of_birth.discard(7)
print(dates_of_birth)
'''


'''
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
print(farm_1.intersection(farm_2))
'''


'''
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_1 = {"dog", "cat", "mouse", "sheep"}
print(farm_2.difference(farm_1))
'''


'''
name={"aman","dos","bakberdi","sanjar","meder"}
name.add("erlan")
print(name)
name.pop()
print(name)
'''



'''
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu.update({'besh_barmak':130})
print(menu)
menu.update({'lagman':135})
print(menu)
'''


'''
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu.update({'drinks':['Coca-Cola', 'Sprite', 'Fanta']})
print(menu)
'''


'''
set ={'add', 'update', 'intersection', 'remove', 'difference', 'intersertion_update', 'clear', 'discard', 'pop' }
dictionary ={'clear', 'get', 'values', 'items', 'update','keys' }
print(set.intersection(dictionary))
'''

'''
south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname','Suriname', 'Uruguay', 'Venezuela']
print(south_american_countries)
ls =set(south_american_countries)
print(ls)
'''


'''
suitcase = []
a =input()
b =input()
d =input()
f =input()
e =input()
suitcase.append(a)
suitcase.append(b)
suitcase.append(d)
suitcase.append(f)
suitcase.append(e)
print(suitcase)
suitcase.pop(4)
print(suitcase)
'''



import random


'''
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
ls = []
for i in range(4):
    l = random.choice(names)
    ls.append(l)

print(ls)
'''

'''
import sys 
print (sys.platform)
'''

ls_for_files = ['qwerty.txt', 'wdhfdkj.py', '122,py', 'index.html', 'd.txt']

for i in range(5):
    f = random.choice(ls_for_files)
    ls_for_files.remove(f)
    with open (f'/home/dosmart/dosmart_1{f}', 'w') as file:
        file.write('Hello!')

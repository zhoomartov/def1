


'''
a =input('язык программипование')
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
	if i == a:
		print("есть")
'''

'''
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
	print(i)
	if i =="php":
		break
'''
'''
a = 1
for i in range(5):
	a = a*7
print(a)
'''


'''
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
a =0 
for i in languages:
        print(a, i)
        a += 1

'''


'''
for i in range(11):
        print(i)
for i in range(9, 0, -1):
        print(i)
'''



'''
names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
for i in range(len( names)):
        if i % 2 == 1:
                print(names[i])


'''

'''
a=int(input("число"))
b=str(a)
print(type(b))
if len(b)==3:
	print('Это число трёхзначное')
if  a>=0  and a%2==0:
        print('это число положительное и четное')
else:
        print('это число отрицательное или не четное')

if a%31 == 0:
        print('это число делится на 31 без остатка')
else:
        print('это число не делится на 31 без остатка')
if a>=100 and a%17==0 or a>=150 and a==13**2:
	print(a)
'''


'''
ls=[]
for i in range(-100, 100):
	ls.append(i)
#print(ls)
for item in (ls):
	if item%13==0 and item%2==0:
		print(item)
		item**2
'''


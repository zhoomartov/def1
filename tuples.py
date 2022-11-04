
'''
a=(123,12.33,435)
b=("dos","dosmart")
c=("amamcho",124124,124.343)
d=("azat","aman",2355)
e=("qwerty",4565)

ls=[]
ls.extend(a)
ls.extend(b)
ls.extend(c)
ls.extend(d)
ls.extend(e)

#print(ls)



print(c[0])
print(c[1])
print(c[2])
#print(a[::1])
'''
'''
ls=[]
ls.append(1234)
ls.append("qwerty")
ls.append(983.32)
ls.append(('asdfg'))
ls.append(['Adinai'])
#print(ls)
'''


'''
ls=['Aigerim', 'Bekmamat', 'Nurbek', 'Azamat','Shirin']
a=' ' 
print(a.join(ls))
'''
'''
numbers = [10, 1, 14.5, 12.0001]
names=['Aigerim', 'Bekmamat', 'Nurbek', 'Azamat','Shirin']
numbers.extend(names)
print(numbers)
'''

#names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
#print(names.count('Jack'))


#names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
#names.remove('Jackson')
#print(names)



'''
ls=[]
ls.append('dosmart')
ls.append(2007)
ls.append("Python")
print(ls)
'''

'''
pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
print(pythonList.index('loop'))
print(pythonList.pop(6))
print(pythonList)
'''


'''
numbers = [123, 321, 2, 543, 64, 463, 234, 867, 6234, 63246, 3, 43]
a =0
for i in numbers:
	a+=i
print(a)
'''



'''
#names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
a='Запуск Ethereum 2.0 состоится 1 декабря. На депозитный контракт внесено более 524 288 ETH'
numbers=[]
letters=[]
for i in a:
	if  i.isdigit():
		letters.append(i)
	elif i.isalpha():
		numbers.append(i)
print(letters)
print(numbers)
'''


pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
print(pythonList[1:4])

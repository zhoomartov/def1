'''
dlina=int(input("длина"))
shirina=int(input("шириина"))
s=dlina*shirina
p=dlina+dlina+shirina+shirina
print("Площадь=",s,"Переметр",p)
'''

'''
ls=[]
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
	if i>5:
		ls.append(i)
print(ls)
'''

'''
ls=[]
for i in range(301):
	#print(i)
	if i <=255:
		if i %2==0:
			ls.append(i)
			print(i)

'''

'''
a = [1,2,2,1,6,4,7,8,6,5]
b = 1
while b != len(a):
	if a[b] > a[b - 1]:
		print(a[b])
	b += 1
'''

'''
area=input("Селекционный,Кок-Жар,Чон арык, Байтик или Ортосай\nвыберите одно:")
r=["Кок-Жар",'Байтик','Ортосай']
for i in r:
	break
	if i==area:
		print("Да,у нас есть дома в этом районе")
		s=["4","3","5","6"]
		ss=input("Сколько сотых земли вы хотели?")
		for item in s:
			if ss==item:
				print("Да есть такие участки")
			else:
				print("К сожелению нет таких участков земли")
	else:
		print("все дома в этом районе проданы")
'''



'''
area=input("Дом нужен в районе чон арык, байтик или ортосай\n")
#print("Да у нас есть дом в районе-",area)
a=input("Дом сделан из чего?")
b=input("Сколько сотох земли?")
if a=="кирпича""кирпич" or b=='4':
	print("Стоимость должна быть не более 50000$")
elif a=="пескаблок" or b=="5":
	print('Стоимость должна быть не более 45000$')
elif a=="кирпича"or b=="5":
	print("Стоимость должна быть не более 55000$")
elif a=="пескаблок" or b=="4":
        print('Стоимость должна быть не более 40000$')
'''
'''
a ='17531'
b = 5821
#for i in len(a):
#print(len(a))
print(3<5821)
'''
'''
a=4388%7
if a>=4:
	print(a*7)
'''

'''
a=4292%5
if a<=3:
	print(a/3)
'''

'''
a=27**3
b=a*3
c=b*5
d=c+7
print(d)
'''


'''
a=183-17
b=a/19
c=b+16.6
d=c*2
print(d%12)
'''

'''
v=input("+,-,/,*,**, //,%\n")
number1 = int(input("число"))
number2 = int(input("число"))
if v== '+':
	print(number1+number2)
elif v== '-':
        print(number1-number2)
elif v== '/':
        print(number1/number2)
elif v== '*':
        print(number1*number2)
elif v== '**':
        print(number1**number2)
elif v== '//':
        print(number1//number2)
elif v== '%':
        print(number1%number2)
'''


'''
users = [ ]
a=input("Регистрация \nвведите логин и пароль: ")
users.append(a)
print(users)
b=input("      Войти \nвведите логин и пароль: ")
for i in users:
	if i==b:
		print("ДОБРО ПОЖАЛОВАТЬ")
	else:
		print("НЕПРАВИЛЬНЫЙ ЛОГИН ИЛИ ПАРОЛЬ")
'''

'''
ls=[]
for i in range(1000):
	if i %3==0:
		ls.append(i)
for item in range(1000):
        if item %5==0:
                ls.append(item)
print(sum(ls))
'''


'''
ls=['python','javascript','java']
a=input("Какой язык програмирования вы знаете")
age=int(input("Сколько вам лет?"))
o=int(input("Опыт работы?"))
for i in ls:
	print()
if o>=3 and age>=18 and age<=65:
	if i==a:
		print("вы подходите")
	else:
		print("вы не подходите нашим требованием")

else:
                print("вы не подходите нашим требованием")
'''

a = [1, 1, 2, 3 ,13, 13, 13, 13, 13, 13, 13, 13, 13, 5, 8, 13, 21, 34,1,55, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 1313, 13, 13, 13, 13, 13, 89]
a.append(13)
print(a.count(13))
print(len(a))
p=(28*100)/40
if p<70:
	print('НЕУЖЕЛИ')
elif p>70:
	print("Я ТАК И ЗНАЛ")
elif p==70:
	print("СОВПАДЕНИЕ ? НЕ ДУМАЮ")

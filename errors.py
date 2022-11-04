'''
number =input('5 чисел с пробелами \n')
num ={}
num=set(num)
for i in number.split():
	num.add(int(i))
print(min(num))
'''

'''
f=input("Python ФУНКЦИЯ")
if f == 'print':
        print('выводит результат')
elif f == 'len':
        l = len(f)
        print(f'len {l}')
elif f == 'append':
        n.append(f)
        print(n,'вот ваш лист')
elif f == 'index':
        print('находит индекс')
elif f == 'add':
        print('добавляет элемент в множество ')
else:
        print('вы непровильно ввели финкцию!!!')
'''


'''
s=int(input("Сколько вы хотите взять в кредит?НЕ МЕНЬШЕ 50 000!!!\n"))
sum=s*(3.47/100)
print(round(sum,2))
'''

'''
try:
        values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
        true= {}
        false = {}
        true = set(true)
        false = set(false)
        for i in values:
                if i:
                        true.add(int(i))
                else:
                        false.add(i)


except:
        for i in values:
                if i:
                        true.add(str(i))
                else:
                        false.add(i)
print('true: ', true)
print('false: ', false)
'''
'''
try:
	a=123
	b="123"
	print(a+b)
except TypeError:
	print('TypeError')


try:
	ls=[]
	for i in range(10):
        	ls.append(i)
	print(ls.pop(1213))

except IndexError:
        print('IndexError')

try:
        a=123
        b=12213
        print(a+xcvb)
except NameError:
        print('NameError')
'''


'''
try:
at = 10
in = 15
wo = 20

for e in range(-at, at):
print(wo / e)
if at > '5':
print("at > 5)
except IndentationError:
	print(SyntaxError)
'''


'''
lst = []
for i in range(10):
	lst.append(i)

a = list(reversed(lst))
sls_obj = slice(0,8)
print(a[sls_obj])
'''

'''
a = 0
b = 1
numbers = []
try:
        while b > a:
                numbers += b
                b += 1
except TypeError:
        print('что-то с типами данных!')

'''

'''
dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
try:
	for x in dict_.keys():
		x + 'abc'
except TypeError:
	print('ind and str')
'''

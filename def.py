
my_list = [1, 'dfkjfhd', True, 555]
def length():
    result = 0
    for i in my_list:
        result += 1
    print('ваш список состоит из {0} элементов'.format(result))

#length()


list_1 = ['name', 'age', '1', '19']

def listik():
    l1 = list_1[: len(list_1)//2]
    l2 = list_1[len(list_1)//2 :]
    l1 = list(reversed(l1))
    l2 = list(reversed(l2))
    print(l1+l2)

#listik()



def fibonachche(chislo):
    list =[]
    a = 0
    b = 1
    for i in range(chislo):
        c = a+b
        list.append(c)
        a = b
        b = c
    print(list)

#fibonachche(10)


def slojenya():
    x=int(input("сложения\nчисло "))
    y=int(input("число"))
    result=x+y
    print(result)

#slojenya()

def vichitanie():
    number1=int(input("вычитание\nчисло"))
    number2=int(input("число"))
    result=number1-number2
    print(result)
#vichitanie()

def colkulyator():
    vichitanie()
    slojenya()

#colkulyator()


def open_file():
    file=input("Названия файл\n")
    with open(file,'w') as b:
        b.write("ВАШ ФАЙЛ")
#open_file()

import random

def gen_number():
    num=['1','4','5','7','9','0']
    number=['0444']
    for i in range(6):
        d =random.choice(num)
        number.append(d)
        number1 = ''.join(number)
    print(number1)

#gen_number()



def maskify(cc):
    newstring = ''
    for character in cc[0:-4]:
        newstring += '#'
    for number in cc[-4:]:
        newstring += number
    return newstring
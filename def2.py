
print((lambda a, b, c: f'Объём бассейна = {a*b*c}')(5, 6, 4))

print((lambda a: f"До нового года осталось {365-a}, прошло с нового года {a}")(303) )

def nechetnye(number):
    if number%2==1:
        print(number)
    nechetnye(number+1)

#print(nechetnye(1))


a={'dos',"dosmart","123",777,"dosya"}

def set_set(kass):
    print(kass)
    if len(kass)==0:
        return kass
    else:
        kass.pop()
        set_set(a)
#print(set_set(a))

import random

numbers=[]
def gen_chislo100(chislo_1):
    for i in range(100):
        random_chislo=random.randint(10,50)
        numbers.append(random_chislo)
    print(numbers)
    def chislo(argument):
        chislo_1(argument)
    return chislo

@gen_chislo100
def delete (argument):
    argument =set(argument)
    print(list(argument))

#delete(numbers)

def registration(f):
    def wrapper(n, p):
        f(n, p)
    return wrapper


@registration
def cache(n, p):
    users = {}
    ls_for_use = []
    ls = []
    for i in n:
        ls.append(ord(i))
    print(ls)
    while len(ls)!=0:
        for i in ls:
            ls.remove(i)
            ls_for_use.append(str(i))
    print(ls_for_use)
    name = ''.join(ls_for_use)
    print(name)
#cache("dosmart","777")



import random 
'''
number = random.randint(1,25)
choices=0
while choices<5:
    print("Угадай число между 1 и 25")
    a=int(input())
    choices+=1
    if a<number:
        print("Мое число больше твоего")
    if a>number:
        print("Мое число меньше твоего")
    if a==number:
        break

if a==number:
    print("Молодец!Ты угадал число с "+str(choices)+"попытки!")
else:
    print("К сожедению ,ты не угадал число.Я загадал"+str(number))
'''

def guess_number():
    tries = 1
    random_number = random.randint(0,10)
    number = int(input('Выберите число в диапазоне от 0 до 10: '))
    if number == random_number:
        print('Вы выиграли!')
    else:
        while random_number != number:
            number = int(input('Попробуйте еще раз! '))
            tries += 1
            if tries == 3:
                print('Вы воспользовались всеми тремя шансами! ВЫ проиграли.Я загадал число:'+str(random_number))
                break
            if number == random_number:
                print('Вы выиграли!')

#guess_number()


'''
for i in range(1,11):
    for item in range(1,11):
       print(i*item,end="\t")
    print()
'''
#print("понидельник\t вторник\t среда\t четвкрг  суббота воскресениья ")
'''
s= input()
aaa=s.split()
fioshort= aaa[0]+ " "+ aaa[1][0]+'.'+aaa[2][0]+'.'
print(fioshort)
'''


import random as rd

def Back_end ():
    p=1
    random_number = rd.randint(0,10)
    print(random_number)
    number=int(input("Любое число от 1 до 10 \nу вас есть три попытки\n"))
    if number==random_number:
        print("Вы угадали с 1 попытки")
    else:
        while random_number != number:
            number=int(input("Попробуйте еще раз\n"))
            p +=1
            if p==3:
                
                print("Вы потратили все 3 попытки!\nЯ загадал",random_number)
                break
            if number==random_number:
                print("Вы угадали c",p,"попытки ")
                break
Back_end()
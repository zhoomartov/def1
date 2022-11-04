def add(a,b):
    return a+b
#print(add(12,12))

def substract(x,y):
    return x-y
#print(substract(12,12))

def multiply(c,d):
    return c*d
#print(multiply(12,12))

def divide(s,f):
    return s/f
#print(divide(12,12))

def collichestvo(b):
    a =0
    for i in b:
        if i == ' ':
            pass
        else:
            a+=1
    return a 
#print(collichestvo('dosmart'))

def direc (**kwargs):
    return kwargs

print(direc(name='dosmart'))
def fact(x):
    
    fac=1
    for i in range(1,x+1):
        fac=fac*i
    return fac
x=int(input('enter number: '))
print(fact(x))
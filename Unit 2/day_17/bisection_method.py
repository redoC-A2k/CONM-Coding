a = float(input("Enter value of a : "))
b = float(input("Enter value of b : "))
fx = input("Enter your equation in terms of x : ")
E = input("Enter value of E or press enter to use default value of 0.0001  ")

if E=='':
    E=0.00001
else :
    E=float(E)
#print(E)    

def f(x):
    return eval(fx)

if f(a)*f(b)<0:
    m=(a+b)/2
    i=1

    while( abs(f(m))>=E):
        print(f"{i} {a} {b} {m} {f(m)}")
        if f(a)*f(m)>0:
            a=m
        else:
            b=m
        m=(a+b)/2
        i+=1
    print(f"{i} {a} {b} {m} {f(m)}")

else:
    print("Enter value of a and b such that f(a)*f(b)<0")

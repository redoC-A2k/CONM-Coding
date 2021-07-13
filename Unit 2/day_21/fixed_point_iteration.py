b = float(input("Enter value of initial guess = "))
gx = input("Enter your g(x) in terms of x = ")
E = input("Enter value of E or press <Enter> to continue with default value as 0.0001 of E = ")

def g(x):
    return eval(gx)

m=g(b)
i=1
while (abs(b-m)>=E):
    print(i,b,m,abs(m-b))
    b = m
    m = g(b)
    i += 1
print(i,b,m,abs(m-b))

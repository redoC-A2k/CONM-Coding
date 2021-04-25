a = float(input("Enter value of a = "))
b = float(input("Enter value of b = "))
fx = input("Enter your equation in terms of x : ")
mystr = "Enter value of E or press <enter> to continue with default value as"
mystr = mystr + " 0.0001 of E : "
E = input(mystr)

if E == '':
    E = 0.0001
else:
    E = float(E)


def f(x):
    x = x
    return eval(fx)


m = (a*f(b)-b*f(a))/(f(b)-f(a))
i = 1
print("i a b m f(m)")
while abs(f(m)) > E:
    print(f"{i} {a} {b} {m} {f(m)}")
    a = b
    b = m
    m = (a*f(b)-b*f(a))/(f(b)-f(a))
    i += 1
print(f"{i} {a} {b} {m} {f(m)}")

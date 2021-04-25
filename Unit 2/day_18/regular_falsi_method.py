a = float(input("Enter value of a = "))
b = float(input("Enter value of b = "))
fx = input("Enter your equation in terms of x : ")
str = "Enter value of E or press <enter> to continue with  default value as"
str = str+" 0.0001 as var: "
E = input(str)

if E == '':
    E = 0.0001
else:
    E = float(E)


def f(x):
    x = x
    return eval(fx)


if f(a)*f(b) < 0:
    m = (a*f(b)-b*f(a))/(f(b)-f(a))
    i = 1
    print(f'{"i a b m fm"}')
    while abs(f(m)) >= E:
        print(f"{i} {a} {b} {m} {f(m)}")
        if f(a)*f(m) > 0:
            a = m
        else:
            b = m
        m = (a*f(b)-b*f(a))/(f(b)-f(a))
        i += 1
    print(f"{i} {a} {b} {m} {f(m)}")
else:
    print("Enter correct value of a and b")

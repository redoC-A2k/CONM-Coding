import sympy as spy

b = float(input("Enter value of initial guess =  "))
fx = input("Enter your equation in terms of x = ")
mystr = "Enter value of E or press <enter> to continue with default value as "
mystr = mystr + " 0.0001 of E : "
E = input(mystr)


if E == '':
    E = 0.0001
else:
    E = float(E)


def f_diff(y, val):
    x = spy.symbols('x')
    diff_str = str(spy.diff(y, x))
    x = val
    return eval(diff_str)


def f(x):
    x = x
    return eval(fx)


m = b - f(b)/f_diff(fx, b)
i = 1
while abs(f(m)) >= E:
    print(f"{i} {b} {m} {f(m)}")
    b = m
    m = b - f(b)/f_diff(fx, b)
    i += 1
print(f"{i} {b} {m} {f(m)}")



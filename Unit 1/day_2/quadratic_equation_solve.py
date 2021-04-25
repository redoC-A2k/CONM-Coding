import math as m
a,b,c = input("Enter value of space saperated value of a, b, c : ").split()
a=float(a)
b=float(b)
c=float(c)

if a==0:
    print("Not a quadratic equation")
    if b==0:
        print("Invalid equation")
    else:
        print("x = ",-c/b)

else :
    D = (b*b) - (4*a*c)
    if D==0 :
        print("Equation has real and equal roots = ",-b/(2*a))
    elif D>0 :
        D = m.sqrt(D)
        print("Roots are real and distinct , 1st root = ",(-b+D)/(2*a), " 2nd root = ",(-b-D)/(2*a))
    else:
        x_real = (-b/(2*a))
        x_img = m.sqrt(abs(D))/(2*a)
        print("Roots are imaginary \n 1st root = ",x_real,"+", x_img,"i and 2nd root = ",x_real,"-",x_img,"i")

coefficients = input("Input format  - a(n)<space>a(n-1)<space>a(n-2)...a(1)<space>a(o) \nNote - a(n)-Coefficient of x(n)\n       a(n-1)-Coefficient of x(n-1)\n     ...\n     ... \n      a(0)-Coefficient of x^0 \n       (Enter zero for coefficient which are not in equation)\nEnter - ")
coefficients = coefficients.split()
coefficients = [float(each) for each in coefficients]
n = coefficients.__len__() - 1
print(coefficients) 
x=float(input("Enter value of x at which to calculate value of fx : "))

polynomial_value = coefficients[n]
n-=1

while n>=0:
    polynomial_value = coefficients[n] + x*polynomial_value
    n-=1

print("value of polynomial is ",polynomial_value)

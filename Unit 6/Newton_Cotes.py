import sympy as spy

def caclulate_fact(i):
    num = 1
    for j in range(1,i):
       num*=j 
    #print(num)
    return num

def f(x,fx):
    return eval(fx)


def calculate_u(i):
    u=spy.symbols('u')
    expr = 1
    for i in range(1,i):
        expr*=u-(i-1)
    return expr

def forward_diff_f(i,a,h,fx):
    i = int(i)
    if i==0:
        return f(a,fx)
    elif i==1:
        return f(a+h,fx)-f(a,fx)
    else:
        return forward_diff_f(i-1,a+h,h,fx)-forward_diff_f(i-1,a,h,fx)

if __name__ == "__main__":
    n=int(input("Enter the value of n for calculation of Newton cotes formulae : "))
    a=float(input("Enter the value of a or lower limit : "))
    b=float(input("Enter the value of b : "))
    s=int(input("Enter the no of segments to break : "))
    fx=input("Enter the equation in terms of x to integrate :")
    h=spy.Rational((b-a)/s).limit_denominator(10000)

    if '^' in fx:
        fx = fx.replace('^', '**')

    calculated_integrated_u_as_n_arr = []
    i=1
    u=spy.symbols('u')
    while True:
        each_u_term = calculate_u(i)
        each_integrated_u_as_n = spy.integrate(each_u_term,(u,0,n))
        #print(each_u_term," , ",each_integrated_u_as_n)
        if each_integrated_u_as_n <= spy.S.Zero :
            break
        each_integrated_u_as_n=each_integrated_u_as_n / caclulate_fact(i)
        calculated_integrated_u_as_n_arr.append(each_integrated_u_as_n)
        i+=1
    print(calculated_integrated_u_as_n_arr)

    result = 0
    for i in range(0,s,n):
        each_result=0
        for counter,each_calculated_integral in enumerate(calculated_integrated_u_as_n_arr):
            forward_diff_part = forward_diff_f(counter, a+i*h, h, fx)
            print(each_calculated_integral,"+",forward_diff_part,end=" ,")
            each_result+=each_calculated_integral * forward_diff_part
        print(" = ",each_result)
        result+=each_result
    print(result)


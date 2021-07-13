import sympy as spy

def caclulate_fact(i):
    num = 1
    for j in range(1,i):
       num*=j 
    return num

#def f(k,fx):
#    x=spy.symbols('x')
#    fx=spy.parsing.parse_expr(fx)
#    return fx.subs(x,k)

def f(x,fx):
    return eval(fx)

def calc_u(i,u):
    num = 1
    for i in range(1,i):
        num*=u-(i-1)
    return num

def forward_diff_fa(i,a,h,fx):
    i = int(i)
    if i==0:
        return f(a,fx)
    elif i==1:
        return f(a+h,fx)-f(a,fx)
    else:
        return forward_diff_fa(i-1,a+h,h,fx)-forward_diff_fa(i-1,a,h,fx)


def each_term_interpolated(a,i,h,fx):
    u = spy.symbols('u')
    expr = 1
    for j in range(1,i):
        expr=expr * (u-int(j-1))
    expr = spy.expand(expr)
    term=forward_diff_fa(i-1,a,h,fx) * expr
    return term

def formulae_after_integrate(k):
    i=1
    n = spy.symbols('n')
    u=spy.symbols('u')
    while True:
       each_term = each_term_interpolated(a,i,h,fx)
       integrated_each_term = spy.integrate(each_term,(u,0,n))
       if (integrated_each_term.subs(n,k)<=0):
           break

if __name__ == "__main__":
    n=int(input("Enter the value of n for calculation of Newton cotes formulae : "))
    a=float(input("Enter the value of a or lower limit : "))
    b=float(input("Enter the value of b : "))
    s=int(input("Enter the no of segments to break : "))
    fx=input("Enter the equation in terms of x to integrate :")
    h=spy.Rational((b-a)/s).limit_denominator(10000)

    for i in range(1,n+1):
        each_term_interpolated(a,i,h,fx)

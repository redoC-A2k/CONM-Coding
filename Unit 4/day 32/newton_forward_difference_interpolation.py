from fractions import Fraction

def calc_u(u,i):
    num=1
    for j in range(0,i):
        num=num*(u-j)
    return num

def calc_fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

if __name__ == "__main__":
    n = int(input("Enter the value of n(no of elements): "))
    diff_2d_arr = [[0]*i for i in range(n,0,-1)]
    diff_x_arr = []
    for i in range(n):
        diff_x_arr.append(int(input("Enter x"+str(i)+" : ")))
        diff_2d_arr[0][i]=float(input("Enter y"+str(i)+" : "))
    x=Fraction(input("Enter the x : "))

    for i in range(1,n):
        for j in range(n-i):
            diff_2d_arr[i][j]=diff_2d_arr[i-1][j+1]-diff_2d_arr[i-1][j]

    print(diff_2d_arr)

    h=diff_x_arr[1]-diff_x_arr[0]
    u=Fraction((x-diff_x_arr[0])/h)

    i=0
    result=Fraction(0)
    while i<n:
        numerator=calc_u(u,i)
        numerator*=diff_2d_arr[i][0]
        denominator=calc_fact(i)
        print(str(Fraction(numerator/denominator))+" + ",end="")
        result+=Fraction(numerator/denominator)
        i+=1
    print(" = "+str(result))
    print(" result in float "+str(float(result)))



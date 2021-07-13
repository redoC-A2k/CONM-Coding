from fractions import Fraction

def calc_num(diff_x_arr,i,x):
    num=1
    for j in range(0,i):
        num=num*(x-diff_x_arr[j])
    return num

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
            num=diff_2d_arr[i-1][j+1]-diff_2d_arr[i-1][j]
            den=diff_x_arr[i+j]-diff_x_arr[j]
            diff_2d_arr[i][j]=Fraction(num/den)

    print(diff_2d_arr)

    i=0
    result=0
    while i<n:
        num=calc_num(diff_x_arr,i,x)
        print(str(num*diff_2d_arr[i][0])+" + ",end="")
        result+=Fraction(num*diff_2d_arr[i][0])
        i+=1
    print(" = "+str(result))
    print(" result in float "+str(float(result)))



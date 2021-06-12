from fractions import Fraction
def format_2d_arr(diff_2dy_arr,n):
    new_2dy_arr=[['     ']*(2*n-1) for i in range(n)]
    for i in range(n):
        start_pos=i
        end_pos=2*n-1-1
        j=0
        while start_pos != end_pos-i+2:
            new_2dy_arr[i][start_pos]=diff_2dy_arr[i][j]
            start_pos+=2
            j+=1
    return new_2dy_arr

if __name__ == "__main__":
    n = int(input("Enter the value of n(no of elements): "))
    diff_2dy_arr = [[0]*i for i in range(n,0,-1)]
    diff_x_arr = []
    for i in range(n):
        diff_x_arr.append(int(input("Enter x"+str(i)+" : ")))
        diff_2dy_arr[0][i]=Fraction(input("Enter y"+str(i)+" : "))

    for i in range(1,n):
        for j in range(n-i):
            num=diff_2dy_arr[i-1][j+1]-diff_2dy_arr[i-1][j]
            den=diff_x_arr[i+j]-diff_x_arr[j]
            diff_2dy_arr[i][j]=Fraction(num/den)
    print(diff_2dy_arr)
    returned_2dy_arr = format_2d_arr(diff_2dy_arr,n)
    for i in range(2*n-1):
        for j in range(n):
            print(returned_2dy_arr[j][i],end=' ',sep='')
        print()

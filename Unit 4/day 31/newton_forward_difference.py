def format_2d_arr(diff_2d_arr,n):
    new_2d_arr=[['    ']*(2*n-1) for i in range(n)]
    for i in range(n):
        start_pos=i
        end_pos=2*n-1-1
        j=0
        while start_pos != end_pos-i+2:
            new_2d_arr[i][start_pos]=diff_2d_arr[i][j]
            start_pos+=2
            j+=1
    return new_2d_arr

if __name__ == "__main__":
    n = int(input("Enter the value of n(no of elements): "))
    diff_2d_arr = [[0]*i for i in range(n,0,-1)]
    for i in range(n):
        mystr="Enter y"+str(i)+" : "
        diff_2d_arr[0][i]=float(input(mystr))

    for i in range(1,n):
        for j in range(n-i):
            diff_2d_arr[i][j]=diff_2d_arr[i-1][j+1]-diff_2d_arr[i-1][j]

    print(diff_2d_arr)
    returned_2d_arr = format_2d_arr(diff_2d_arr,n)
    for i in range(2*n-1):
        for j in range(n):
            print(returned_2d_arr[j][i],end=' ',sep='')
        print()

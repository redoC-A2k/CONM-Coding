from fractions import Fraction
def calc_num(y,n,y_arr,index_hidden):
    num=Fraction(1)
    for i in range(n):
        if i != index_hidden:
            num*=y-y_arr[i]
    return num

if __name__=="__main__":
    x_arr=[]
    y_arr=[]
    n=int(input("Enter the value of n : "))

    for i in range(n):
        x_arr.append(Fraction(input("Enter x"+str(i)+" : ")))
        y_arr.append(Fraction(input("Enter y"+str(i)+" : ")))

    y=Fraction(input("Enter y :"))

    i=0
    result=0
    while i<n:
        numerator = calc_num(y,n,y_arr,i)
        denominator = calc_num(y_arr[i],n,y_arr,i)
        num=Fraction(numerator/denominator)
        num*=x_arr[i]
        result+=num
        print(str(num),end=" + ")
        i+=1
    print("\b\b\b = "+str(result))
    print("result in floating is ",float(result))

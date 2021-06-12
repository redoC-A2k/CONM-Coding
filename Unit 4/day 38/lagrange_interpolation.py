from fractions import Fraction
def calc_num(x,n,x_arr,index_hidden):
    num=Fraction(1)
    for i in range(n):
        if i != index_hidden:
            num*=x-x_arr[i]
    return num

if __name__=="__main__":
    x_arr=[]
    y_arr=[]
    n=int(input("Enter the value of n : "))

    for i in range(n):
        x_arr.append(Fraction(input("Enter x"+str(i)+" : ")))
        y_arr.append(Fraction(input("Enter y"+str(i)+" : ")))

    x=Fraction(input("Enter x :"))

    i=0
    result=0
    while i<n:
        numerator = calc_num(x,n,x_arr,i)
        denominator = calc_num(x_arr[i],n,x_arr,i)
        num=Fraction(numerator/denominator)
        num*=y_arr[i]
        result+=num
        print(str(num),end=" + ")
        i+=1
    print("\b\b\b = "+str(result))
    print("result in floating is ",float(result))

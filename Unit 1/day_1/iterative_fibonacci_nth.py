n = int(input("Enter the value of n"))

if n<1:
    print(0)
else:
    if n==1:
        print(1)
    else :
        fib2 = 0
        fib1 = 1
        fib = 0

        for i in range(2,n+1):
            fib = fib1+fib2
            fib2 = fib1
            fib1 = fib

        print(fib)

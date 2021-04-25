x1=float(input("Enter value of x1"))
x2=float(input("Enter value of x2"))
e1=float(input("Enter value of e1"))
e2=float(input("Enter value of e2"))

k=abs(e1-e2)

if e1>e2:
    x2=x2/(10**k)
    e=e1
else:
    x1=x1/(10**k)
    e=e2
x=x1+x2

if x>=1:
    x=x/10
    e+=1

if e>99:
    print("Overflow occured")
else:
    print(f"The answer is {x}E{e}")
    

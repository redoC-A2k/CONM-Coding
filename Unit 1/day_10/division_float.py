x1 = float(input(("Enter value of x1 : ")))
e1 = float(input(("Enter value of e1 : ")))
x2 = float(input(("Enter value of x2 : ")))
e2 = float(input(("Enter value of e2 : ")))

x = x1/x2
e = e1-e2

if abs(x) < 0.1:
    x = x*10
    e = e-1

if abs(x) > 1.0:
    x = x/10
    e += 1

if e > 99:
    print("overflow")
elif e < -99:
    print("Underflow")
   
print(f"The answer is {x}E{e}")

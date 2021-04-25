n = int(input("Enter value of n = "))
matrix = []
for i in range(n):
    a = []
    for j in range(n+1):
        print("Enter value of a[", i, "]", "[", j, "]", end=" : ")
        a.append(float(input()))
    matrix.append(a)

max_itr = int(input("Enter the value of iterations : "))
e = float(input("Enter the value of err : "))

x = []
for i in range(n):
    x.append(0.0)

for k in range(1, max_itr+1):
    big_E = 0
    for i in range(n):
        sum = 0.0
        for j in range(n):
            if i != j:
                sum += matrix[i][j]*x[j]
        temp = (matrix[i][n] - sum) / matrix[i][i]
        rel_error = abs((temp - x[i])/temp)
        x[i] = temp
        
        if (rel_error > big_E):
            big_E = rel_error
   
    print(f"itr - {k}", end=", ")
    for i in range(n):
        print(round(x[i], 4), end=", ")
    print("big_error", big_E)
    
    if big_E <= e:
        print("solution converges in ", k, "iterations")
       

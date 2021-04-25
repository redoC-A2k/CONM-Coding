n = int(input("Enter value of n = "))
matrix = []
for i in range(n):
    a = []
    for j in range(n+1):
        print("Enter value of a[", i, "]", "[", j, "]", end=" : ")
        a.append(float(input()))
    matrix.append(a)

max_itr = int(input("Enter the value of iterations : "))
Error = float(input("Enter the value of err : "))

old_x = []
for i in range(n):
    x = input("initial_guess[i] - ")
    if x == '':
        x = 0
    else:
        x = float(x)
    old_x.append(x)

big_Error = 0
for k in range(1, max_itr+1):
    new_x = []
    rel_error = 0
    big_Error = 0
    for i in range(n):
        sum = 0.0
        for j in range(n):
            if i != j:
                sum = sum + matrix[i][j]*old_x[j]
                print("Sum = ",sum,end=",")

        new_x.append((matrix[i][n] - sum)/matrix[i][i])
        try:
            rel_Error = abs((new_x[i] - old_x[i])/new_x[i])
        except Exception as e:
            print("Exception the value of one of the variable is zero", e.__str__())
            rel_Error = 0

        if rel_Error > big_Error:
            big_Error = rel_Error

    if big_Error <= Error:
        print("Solution is convergent it converges in ", k, "iterations")
    print(f"itr - {k}th", end=", ")
    for i in range(n):
        print(round(new_x[i], 4), end=',')
    print("rel_error ", big_Error)

    for i in range(n):
        old_x[i] = new_x[i]
if big_Error > Error:
    print("Solution does not converges in ", max_itr, " iterations")

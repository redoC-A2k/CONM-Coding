n = int(input("Enter value of n = "))

matrix = []

for i in range(n):
    a = []
    for j in range(n+1):
        print("Enter value of a[", i, "]", "[", j, "]", end=" : ")
        a.append(float(input()))
    matrix.append(a)

k = 0
while k < n:
    i = 0
    while i < n:
        u = matrix[i][k]/matrix[k][k]
        j = k
        if i != k:
            while j < n+1:
                matrix[i][j] = matrix[i][j] - matrix[k][j]*u
                j += 1
        i += 1
    k += 1

for i in range(n):
    for j in range(n+1):
        print(matrix[i][j], end='   ')
    print()

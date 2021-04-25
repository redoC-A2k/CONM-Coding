mystring = input("Enter space saperated numbers: ")
mylist = mystring.split(' ')
int_list = [int(element) for element in mylist]
sum = 0

for x in int_list:
    sum=sum+x

print(sum)

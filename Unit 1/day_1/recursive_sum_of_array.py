def sum_of_array(array,length):
    """returns sum of array in recursive way"""
    if length < 0:
        return 0.0
    else :
        return sum_of_array(array,length-1)+array[length]

mystring = input("Enter space saperated numbers")
mystring  = mystring.split()
myList = [ float(x) for x in mystring ] 

print("sum = ",sum_of_array(myList,len(myList)-1))

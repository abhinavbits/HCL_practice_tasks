import sys
#The function will assert if two arguments are equal and exits with an error message if they are not.
def assertEqual(a, b, error = "Error!"):
    if(type(a) != type(b)): 
        print(error)
        sys.exit()
    if(a==b):
        print("Assertion is succesful!")
        return 1
    else:
        print(error)
        sys.exit()

dic1 = {'foo': 1, 'bar': 2}
dic2 = {'foo': 1, 'bar': 2}
print(assertEqual(dic1, dic2, "Failure!"))

list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 4, 5, 6, 7, 8]
print(assertEqual(list1, list2))

set1 = {"apple", "banana", "cherry"}
set2 = {"cherry", "apple", "banana"}
print(assertEqual(set1, set2))

#Using the function in a loop
arr1 = [1,2,3,4,6]
arr2 = [1,2,3,5,6]
newList = []
for i in range(len(arr1)):
    if(assertEqual(arr1[i], arr2[i], "Element at " + str(i) + " position is not the same!")):
        newList.append(arr1[i])
print(newList)

#Verifying the function for a custom object
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

ob1 = ComplexNumber(3,4)
ob2 = ComplexNumber(3,3)

assertEqual(ob1, ob2, "Object instances have different values")

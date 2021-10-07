def assertEqual(a, b, error):
    if(type(a) != type(b)): 
        print(error)
        return 0
    if(a==b):
        print("Assertion is succesful!")
        return 1
    else:
        print(error)
        return 0

dic1 = {'foo': 1, 'bar': 2}
dic2 = {'foo': 1, 'bar': 2}
print(assertEqual(dic1, dic2, "Failure!"))

list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 4, 5, 6, 7, 8]
print(assertEqual(list1, list2, "Failure!"))

set1 = {"apple", "banana", "cherry"}
set2 = {"cherry", "apple", "banana"}
print(assertEqual(set1, set2, "Failure!"))

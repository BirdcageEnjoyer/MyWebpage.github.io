import random

#initialising array-
array1 = [random.randint(0, 100) for i in range(50)]

print(array1)

#define function
def forLoopLinearSearch(array):
    dataItem = int(input("enter what number you want to find"))  
    for _ in range(len(array)):
        if array[_] == dataItem:
            return _, dataItem
    return -1, "notfound"

print(forLoopLinearSearch(array1))


import random

array1 = [random.randint(0, 40) for i in range(50)]

print(array1)

def whileLoopLinearSearch(array):
    dataItem = int(input("enter which number to find"))
    count = 0
    while count < len(array):
        if array[count] == dataItem:
            return count, array[count]
        else:
            count += 1
    return -1, "not found"

    
print(whileLoopLinearSearch(array1))
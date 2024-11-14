#bubble sort































arrayTest = [2, 3, 5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(arrayTest)
item = int(input("enter number to find"))

def binarySearch2(array, requestedItem):
    length = len(array)
    sPointer = 0
    ePointer = length-1
    while sPointer <= ePointer:
        mPointer =(sPointer + ePointer)//2
        if array[mPointer] == requestedItem:
            return mPointer, requestedItem
        else:
            if requestedItem > array[mPointer]:
                sPointer = mPointer + 1
            else:
                ePointer = mPointer - 1
            
    return -1
    




print(binarySearch2(arrayTest, item))


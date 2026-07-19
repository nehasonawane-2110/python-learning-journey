# Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

def separateEvenOdd(li):
    evenList = []
    oddList = []
    for i in range(len(li)):
        if (li[i] % 2 == 0):
            evenList.append(li[i])    # add even element to even list
        else:
            oddList.append(li[i])
    return evenList, oddList


li = [10, 21, 20, 15, 60, 100, 12, 11]
evenList, oddList = separateEvenOdd(li)
print("Even List", evenList)
print('Odd List', oddList)
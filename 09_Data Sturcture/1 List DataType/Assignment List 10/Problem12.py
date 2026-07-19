# Write a program to print list after removing even numbers.

def removeEvenNumbers(li):
    newList = []
    for i in range(len(li)):
        if (li[i] % 2 != 0):  # check if element is odd
            newList.append(li[i])  # add odd element to new list
    return newList

li = [10, 21, 20, 15, 60, 100, 12, 11]
res = removeEvenNumbers(li)
print(res)
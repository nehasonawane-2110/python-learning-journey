# Write a program to remove all occurrences of a given element in the list.

def removeElements(li, element):
    newList = []
    for i in range(len(li)):
        if (li[i] != element):   # if element is not equal to current element of list
            # != is used to check if element is not equal to current element of list
            newList.append(li[i])   # add element in the new list
    return newList

li = [ 10, 20, 30, 40, 50, 60, 4, 10, 20, 30, 40]
element = 10  # element which we want to remove from list
res = removeElements(li, element)
print(res)
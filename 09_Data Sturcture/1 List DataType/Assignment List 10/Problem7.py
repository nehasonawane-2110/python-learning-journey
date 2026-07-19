# Write a program to create a duplicate of an existing list. It should not point to the same list.

def duplicateList(li):
    newList = []
    for i in range(len(li)):
        newList.append(li[i])  # add each element of original list to new list
    return newList

li = [ 10, 20, 30, 40, 60, 100, 10, 20]
print("original List", li)
res = duplicateList(li)
print("duplicate  List", res)
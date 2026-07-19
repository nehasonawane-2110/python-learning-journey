# 6. Write a program to create a new list from existing list which contains cube of
# each number of list.


def cubeList(li):
    newList = []
    for i in range(len(li)):
        cube = li[i] ** 3  # calculate cube of each element
        newList.append(cube)   # add cube of new line
    return newList

li = [2, 4, 5, 7, 8]
res = cubeList(li)
print(res)
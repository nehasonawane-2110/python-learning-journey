# Write a program to create three lists of numbers, their squares and cubes

def createLists(li):
    squares = []
    cubes = []
    for i in range(len(li)):
        squares.append(li[i] ** 2)  # add square of each element to squares list
        cubes.append(li[i] ** 3)
    return squares, cubes

li = [2, 3, 4, 5, 6, 7, 8]
res = createLists(li)
print("Squares List", res[0])   # res[0] will have squares list
print("Cubes List", res[1])    # res[1] will have cubes list
# 3) Python Program to Sort the List According to the Second Element in Sublist

li = [[1, 3], [4, 1], [2, 5]]

n = len(li)

for i in range(n):
    for j in range(0, n - i - 1):  # loop through the list and compare adjacent elements
        # compare second element
        if li[j][1] > li[j + 1][1]:
            # swap
            li[j], li[j + 1] = li[j + 1], li[j]

print(li)

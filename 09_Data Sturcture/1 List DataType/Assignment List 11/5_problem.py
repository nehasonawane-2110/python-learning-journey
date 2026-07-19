# 5) Python Program to Sort a List According to the Length of the Elements within the list.
# (Bubble Sort)

li = ['apple', 'banana', 'kiwi', 'graps', 'orange']
n = len(li)
for i in range(n):
    for j in range(0, n - i - 1):
        if (len(li[j]) > len(li[j + 1])):   # compare the length of the elements
            li[j], li[j + 1] = li[j + 1], li[j]    # swap if the length of the current element is greater than the next element
print(li)

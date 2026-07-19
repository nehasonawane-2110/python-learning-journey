# 2.Write a program to reverse the list.

def reverseList(li):
    rev = []
    for i in range(len(li)-1, -1, -1):  # range(start, stop, step)
        rev.append(li[i])
    return rev


li = [10, 20, 30, 40, 50]
res = reverseList(li)
print(res)

### range(len(li)-1, -1, -1)
# -start from last index
# -go till index 0
# -move backwards


### rev = [] → empty list
# You are taking elements from last to first
# append() is used to add each element into new list
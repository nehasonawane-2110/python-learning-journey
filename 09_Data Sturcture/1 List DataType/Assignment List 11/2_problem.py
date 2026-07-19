# 2) Python Program to Merge Two Lists and Sort it

def mergeAndSort(li1, li2):
    merged = li1 + li2
    merged.sort()   # sort() method will sort the list in ascending order by default
    return merged

li1 = [5, 3, 1, 2]
li2 = [8, 0, 1, 2]
res = mergeAndSort(li1, li2)
print("merged and sorted list:", res)

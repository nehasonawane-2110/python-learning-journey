# 7) Python Program to Find the Intersection of Two Lists

li1 = [1, 2, 3, 4, 5]
li2 = [3, 4, 5, 6, 7, 8]
res = list(set(li1).intersection(set(li2)))  
# set() will remove duplicates and intersection() will give the common elements from both lists
print("Intersection of the two lists is:", res)
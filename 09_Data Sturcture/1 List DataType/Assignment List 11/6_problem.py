# 6) Python Program to Find the Union of two Lists

li1 = [1, 2, 3, 4, 6]
li2 = [2, 3, 4, 10, 20, 30, 40]
result = list(set(li1).union(set(li2))) 
# set() will remove duplicates and union() will give the unique elements from both lists
print("Union of the two lists is:", result)

# Write a Python program to find elements in a given set that are not in another set.

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 6}
result = set()  # empty set to store the result
for i in set1:
    if i not in set2:
        result.add(i)

print("Element in set1 but not in set2:", result)

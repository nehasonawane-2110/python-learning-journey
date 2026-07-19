# Set Methods -

s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

# 1) add() - add one element
s1.add(80)
print(s1)

# 2) clear() - Remove all element
# example
# s1.clear()
# print(s1)

# 3) copy () - create copy of set(shallow copy)
s3 = s1.copy()
print(s3)

# 4) difference() - element in first set but not in second set
#print(s1.difference(s2))

# 5) difference_update () - it update the set by removing common elements that are present in another set
#s1.difference_update(s2)
#print(s1)

# 6) discard () - remove elements no error if not found
s1.discard(10)
print(s1)

# 7) intersection() - common elements
print(s1.intersection(s2))

# 8) intersection_update() - it update the set by keeping element that are present in both set
s1.intersection_update(s2)
print(s1)

# 9) isdisjoint() - it check wherther two set have no common element
s3 = {700, 80}
print(s1.isdisjoint(s3))
print(s1.isdisjoint(s2))

# 10) issubset() - check whether all  elements of one set are present in another set
s4 = {10, 20}
print(s1.issubset(s2))
print(s4.issubset(s1))

# 11) issuperset() - check whether one set contains all elements of another set
print(s1.issuperset(s4))

# 12) pop() - remove random element
s1.pop()
print(s1)

# 13) remove() - remove element which you want give error if element not present
# s1.remove(20)
# print(s1)

# 14) symmetric_different() - retuen elements that are in either set but not in both
print(s1.symmetric_difference(s2))

# 15) symmetric_differen_update() - it update the original set by keeping element that are in either set but not common
s1.symmetric_difference_update(s2)
print(s1)


# 16) update - is used to add multiple ele in set
s1.update([100,200])
print(s1)

# 17) union - return a set containing all elements from both set (no duplicates)
print(s1.union(s2))

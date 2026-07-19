# Frozenset Method -

s1 = frozenset({10, 20, 30, 40})
s2 = frozenset({30, 40, 50})

# 1) copy() - return copy of frozenset s1
s3 = s1.copy()
print(s3)

# 2) difference()  remove same ele of s2 from s1 give remin in s1
print(s1.difference(s2))

# 3) intersection () return same el in both frozenset
print(s1.intersection(s2))

# 4) isdisjoint() -
# return true if all ele are diff in both set
print(s1.isdisjoint(s2))

# 5) issubset() - return true if all elements of s1 in s2
print(s1.issubset(s2))

# 6) issuperset() - return true all ele od s2 in s1 
print(s2.issuperset(s1))

# 7) symmetric_difference() - return diff elements in both set
s1.symmetric_difference(s2)
print(s1)

# 8) union () - return all ele fron both set excluding duplicate
s1.union(s2)
print(s1)
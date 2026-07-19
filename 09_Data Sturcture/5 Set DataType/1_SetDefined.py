# Set Data Type -
# set is a collection used to store unique elements(No duplicate allowed)

# 1) Structure -
# -Denoted by Curly braces {}
# - {}  with only value
# - for blank set use set()
# example -
s = {1, 'a', 'b', 3.14, 10}
print(s)
print(type(s))
s = set()   # blank set
print(s)

## 2) Type of Data - (Heterogenous)
# - can store different types of data
# example -
s = {10, 'a', 'b', 3.16}
print(s)

# 3) sequence - (unordered)
# - set is unordered 
# - No indexing (you cannot use s[0])
# example -
s = {10, 'a', 'b', 20}
print(s)

# 4) chnagable  ( mutable)
# - Not editable
# - mutable but not editable (add , deleted)
s.add(50)
print(s) 

# 5) unique elements are present
s = {1, 'a', 'r', 10, 20, 10, 3.10}
s.add(100)
print(s)

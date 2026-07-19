# Indexing (positive, negative indexing)(len(function))

# - Indexing Means accessing elements of sequence (like list, string, tuple) using there position(index Numbers)

# Two types of indexing -
# 1) Positive Indexing
# 2) Negative Indexing

# 1) Positive Indexing - 
# - Start from 0
# - flow move from Left to Right --> 0, 1, 2, 3, 4
# example -

my_list = [10, 20, 30, 50, 60]
print(my_list[0])
print(my_list[1])


### Last element index total number of elements -1 
print(my_list[-1])  # find last elements

### Total number of elements find in the list -
# - len() function used to find total number of elements in a sequence
# - len() return the length(size) of the object (number item in the list)
# example -

my_list = [10, 20, 30, 40, 50, 60]
num = (len(my_list))
print(num)


### 2) Negative Indexing -
# - start from -1
# - flow move from Right to Left --> -1, -2, -3, -4, -5
# example -
my_list = [10, 20, 30, 50, 60]
print(my_list[-1])

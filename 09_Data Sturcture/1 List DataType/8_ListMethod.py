# List Methods
# - list method are built-in functions that perform specific operations on list.

li = [10, 30, 20, 50, 40]
# 1. append() - add element at the end of the list
li.append(60)
print(li)

# 2.clear() - Remove all elements from the list
li.clear()
print(li)

# 3. copy() - Copy li in new variable. li1 will not change when li is changed
li = [10, 30, 20, 50, 40]
li1 = [20, 10, 30, 50]
li1 = li.copy()
print(li1)

# 4. count() - Gives count of given number, if ele not present gives 0.
count = li.count(50)
print(count)

# 5 extend() - add elements of one list to another list
li2 = [100, 200, 500]
li.extend(li2)
print(li)

# 6.index() - gives index of first occurrence of given element, if ele not present gives error
index = li.index(30)
print(index)

# 7. insert() - add element at specific index
li.insert(2, 25)
print(li)

# 8. pop() - remove and return element at given index, if index not given removes last element
remove = li.pop(4)
print(remove)
print(li)

# 9. remove()- remove first occurrence of given element, if ele not present gives error
li.remove(25)
print(li)


# 10. reverse() -reverse the order of elements in the list
li.reverse()
print(li)

# 11. sort()- sort the elements of the list in ascending order by default, if reverse = True sort in descending order
li.sort()
print(li)
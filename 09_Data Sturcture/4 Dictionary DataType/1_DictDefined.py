# 2 Dictionary DataType 
# - A Dictionary is an data structure used to store data in key-value pairs.
# - collection of key and value

### 1) Structure -
# - Dictionary is denoted by Curly Braces {}.
# Each item has key : value
# Example -
student = {"name": "Radha", "age": 22, "Course": "Python"}
print(type(student))
print(student)

### 2) Types of Data - (Heterogeneous)
# - Dictionary can store different types of data (Heterogeneous)
# - pairs of key: value - heterogeneous
# Example -

Data = {"name": "Radha", "age": 22, 1: "python"}
print(type(Data))
print(Data)

### 3) Sequence - (ordered)
# - Dictionaries are before python 3.6 were unordered, but from python 3.7 onwards they are ordered.
# - ordered - each element has a fixed position in the dictionary
# example -

student = {"name": "Radha", "age": 22, "Course": "Python"}
print(student)

### 4) Changeable - (Mutable)  (key are immutable , value are mutable)
# mutable - you can change(modify), add , delete item in the dictionary after its creation.
# In dictionary - Index is user defined (key
# Example -

student = {"name": "Radha", "age": 22, "Course": "Python"}
print(student["name"])
student['age'] = 23   # update value
print(student)
student["city"] = "bangalore"      # add new key value pair
print(student)


### 5) only immutable data Stucture can be allowed
# Example -
# student1 = {'name': "Neha", [1, 2, 3]: "python"}  # this will give error because list is mutable and it cannot be used as key in dictionary

### 6) key should be unique , duplicate value can be allowed
# Example - 
Data = {1: "python", 2: "java", 2: "c"}  # why output is {1: 'python', 2: 'c'} because key should be unique in dictionary and if we have duplicate key then the last value will be considered for that key.
print(Data)
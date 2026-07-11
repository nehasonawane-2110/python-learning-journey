# dataTypes in python

# The type of the data we have using in the programming.
# A data types tells what kind of value variable hold such as number, text, list.
# In the python everthing is an object and every object has the data types.

# NUMERIC TYPES

""" Whole numbers, positive or negative, without decimals.
   Numeric types include integers, floats, and complex numbers.
   Examples 10,-20,"""

# 1. INT (Integer)
i = 20
print(type(i))

# 2. FLOAT
"""Numbers with a decimal point.
examples 10.0,-20.1"""
i = 3.14
print(type(i))

# 3. COMPLEX
"""Numbers with a real and imaginary part.
examples 3+3j, -2.5+ 4.5j"""
i = 3 + 4j
print(type(i))


# TEXT
"""Sequence of Unicode characters (text).
Enclosed in single ' or double " quotes.
Example: "Hello", 'Python'"""

# 1. STR (string)
i = 'Neha Sonawane'
print(type(i))
i = "Neha sonawane"
print(type(i))
i = '''Neha sonawane'''
print(type(i))
i = """Neha sonawane"""
print(type(i))
# why they all quotes are because some time we used apostrophe (student's)
# in string then it will give error so we can use double, triple,double-triple quotes to avoid error

i = "Student's Data"
print(type(i))


# SEQUENCE
"""Ordered, mutable (changeable), and allows duplicate values.
Elements can be of different types.
Example: [1, "apple", 3.14]"""
# 1. LIST
i = [1, 2, 3, 4, 5]
print(type(i))

# 2. TUPLE
"""Ordered, immutable (unchangeable), allows duplicates.
Example: (1, "banana", 4.5)"""
i = (1, 2, 3, 4, 5)
print(type(i))

# 3. RANGE
"""Represents a sequence of numbers.
Often used in loops.
Example: range(0, 5)"""
i = range(5)
print(type(i))


# MAPPING
"""Unordered collection of key-value pairs.
Keys must be unique.
Example: {"name": "Alice", "age": 25}
"""
# 1. DICT (dictionary)
i = {"name": "Neha", "age": 25}
print(type(i))


# SET
"""Unordered collection of key-value pairs.
Keys must be unique.
Example: {"name": "Alice", "age": 25}"""
# 1. SET
i = {1, 2, 3, 4, 5}
print(type(i))

# 2. FROZENSET
"""Same as set, but immutable (can’t be changed after creation).
Example: frozenset([1, 2, 3])"""
i = frozenset({1, 2, 3, 4, 5})
print(type(i))


# BOOLEAN
"""Represents True or False values.
Used in conditions and logic.
Example: True, False"""
# 1. BOOL
i = True
print(type(i))
i = False
print(type(i))


# NONE TYPE

# 1. NoneType
i = None
print(type(i))

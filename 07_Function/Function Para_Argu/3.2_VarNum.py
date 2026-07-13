# 3) Variable number of arguments / Variable length Parameter.
# Example -
# 1. Mentioned asterisk(*) symbol before parameter in function defination.
# 2. we can pass multiple value in function call.
# 3. We're going to iterate value using for loop
# Addition of numbers -

def add(*data):
    sum = 0
    for ele in data:
        sum += ele
    print(sum)


add(10, 20)
add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

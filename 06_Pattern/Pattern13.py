# Marging Patterns
# we can marge pattern to make a new pattern.

# * $ $ $ $ $
# * * $ $ $ $
# * * * $ $ $
# * * * * $ $
# * * * * * $

for i in range(1, 6):
    for j in range(1, i + 1):  # print the first pattern (increasing pattern)
        print("*", end=" ")
    for j in range(1, 7-i):    # print second pattern(decreasing pattern)
        print("$", end=" ")
    print()

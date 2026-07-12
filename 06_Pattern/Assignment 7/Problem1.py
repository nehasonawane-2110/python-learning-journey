# Kajikatli (Hollow Diamond) Pattern

n = 5

# Upper part
for i in range(1, n + 1):

    # spaces
    for j in range(n - i):
        print(" ", end=" ")

    # stars and hollow spaces
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


# Lower part
for i in range(n - 1, 0, -1):

    # spaces
    for j in range(n - i):
        print(" ", end=" ")

    # stars and hollow spaces
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
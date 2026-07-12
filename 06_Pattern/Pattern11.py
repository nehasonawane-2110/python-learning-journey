# condtion Pattern
# $ $ $ $ $
# * * * * *
# $ $ $ $ $
# * * * * *
# $ $ $ $ $

for i in range(1, 6):
    for j in range(1, 6):
        if (i % 2 == 0):   # even row (*)
            print('*', end=" ")
        else:       # odd row ($)
            print('$', end=" ")
    print()

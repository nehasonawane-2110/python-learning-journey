# Hologram pattern

for i in range(1, 6):
    for j in range(1, i + 1):  # incrementing pattern so 1 to 5
        if (j == 1 or j == i or i == 5):   # condition to print star at the beginning, end and last row
            print('*', end=" ")
        else:
            print(' ', end=" ")
    print()
    
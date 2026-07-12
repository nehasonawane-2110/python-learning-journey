# pyramid

for i in range(1, 6):   # outer for loop for rows
    for j in range(1, 6 - i):     # decrementing spaces
        print(' ', end=" ")      # printing spaces
    for j in range(1, i + 1):    # incrementing stars
        print('*', end="   ")     # add two spaces after each star for alignment
    print()   # new line after each row

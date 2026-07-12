# wap to print the decrement pattern
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(1, 6):
    for j in range(1, 7-i):  # print j inner loop form 1 to 7 -i
        print('*', end=' ')
    print()

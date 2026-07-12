# WAP to print the following pattern 
# A B C D E
# B C D E
# C D E
# D E
# E

for i in range(1, 6):
    for j in range(1, 7-i):
        print(chr(64+i+j-1), end=" ")  # 64 is constant value 
    print()

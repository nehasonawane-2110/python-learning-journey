# WAP to print the following pattern
# A A A A A
# B B B B B
# C C C C C
# D D D D D
# E E E E E

for i in range(1, 6):
    for j in range(1, 6):
        print(chr(64+i), end=" ")  # used chr() function to convert the ASCII value to character.
        # 64 is the constant value to get the corresponding uppercase letter(A=65, B=66, C=67, D=68, E=69).
    print()

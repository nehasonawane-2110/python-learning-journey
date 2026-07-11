# Write a program to input any alphabet and check whether it is vowel or consonant.

alpha = (input("Enter the alphabet: "))
if (alpha == 'a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u' or
    alpha == 'A' or alpha == 'E' or alpha == 'I' or alpha == 'O' or alpha == 'U'):
    print(f'{alpha} is vowel alphabet.')

else:
    print(f'{alpha} is consonant alphabet.')

# another method to solve this problem.
'''
if (alpha in 'aeiouAEIOU'):
    print(f'{alpha} is vowel alphabet.')
else:
    print(f'{alpha} is consonant alphabet.')
'''
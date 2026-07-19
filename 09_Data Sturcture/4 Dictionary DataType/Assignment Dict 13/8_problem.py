# 8) Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

text = "apple banana apple orange banana apple"

words = text.split()  # split() method will split the string into a list of words based on whitespace
freq = {}

for word in words:  # iterate through each word in the list of words
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)
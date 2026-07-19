# Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set
# data type.

# Input string
str = 'python is an is language'

# convert string into list
li = str.split()
un_word = []
for word in li:
    if word not in un_word:
        un_word.append(word)
print("Unique Words:", un_word)

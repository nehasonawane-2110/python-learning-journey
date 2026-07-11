# Nested if- else condition statement
# number categorize greater than or less than or equal to zero.

num = int(input("Enter the number: "))

if (num > 0):
    if (num > 50):
        if (num > 100):
            if (num > 150):
                if (num > 200):
                    print("Number is greater than 200.")
                else:
                    print("Number is greater than 150 but less than 200.")
            else:
                print("Number is greater than 100 but less than 150.")
        else:
            print("Number is greater than 50 but less than 100.")
    else:
        print("Number is greater than 0 but less than 50.")
else:
    print("Number is less than or 0.")

# pass keyword -
# -To neglect the indentation error.
# -It does nothing when executed.
# It is used as a placeholder where a statement is syntactically required but you don’t want to write any code yet.
# - Python does not allow empty blocks.
# -Using pass makes it valid:
#     if True:
#       pass

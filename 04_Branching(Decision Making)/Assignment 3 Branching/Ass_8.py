# Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)
'''
import random       

captcha = random.randint(1111, 9999)
print("Captcha:", captcha)

user_input = int(input("Enter the captcha: "))
'''


import random

userId = (input("Enter the user id: "))
password = int(input("Enter the password: "))

if (userId == 'admin' and password == 12345):
    print("Login successful.")
else:
    print("Not a valid user id and password.")

    captcha = random.randint(1111, 9999)
    print("Captcha:", captcha)

    user_input = int(input("Enter the captcha: "))

    if user_input == captcha:
        print("Success! Captcha matched.")
    else:
        print("failed")

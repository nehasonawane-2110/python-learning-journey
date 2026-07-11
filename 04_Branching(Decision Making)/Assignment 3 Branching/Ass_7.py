# write the program to check if user has entered correct userid and password.

userid = (input("Enter the user id: "))
password = str(input("Enter the password: "))

if (userid == 'Neha' and password == 'Neha@2004'):   # hardcoded value (admin, 12345) means diect take value.
    print("Login successful.")
else:
    print("Not a valid user id and password.")

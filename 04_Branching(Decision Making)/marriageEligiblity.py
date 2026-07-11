# Marriage Eligiblity criteria  (if-else condition statement)

gender = input("Enter gender(M/F): ")   # int not used because string value taken
age = int(input("Enter age: "))

if ((gender == 'M' and age >= 21) or (gender == 'F' and age >= 18)):
    print("You are eligible for marriage.")
else:
    print("Pehle Jindagi ji lo.")

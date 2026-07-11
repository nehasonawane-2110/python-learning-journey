# calculates amount of notes (minimum number of notes)

amount = int(input("Enter amount to calculate minimum number of notes:"))
temp = amount
twoThousands = temp // 2000
temp = temp % 2000
fiveHundreds = temp // 500
temp = temp % 500
hundreds = temp // 100
temp = temp % 100
fifties = temp // 50
temp = temp % 50
tens = temp // 10
temp = temp % 10

print(f'Amonut:{amount}')
print(f'2000s:{twoThousands}, 500s:{fiveHundreds}, 100s:{hundreds}, 50s:{fifties}, 10s:{tens}')

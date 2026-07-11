# Write a program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill



units = int(input("Enter the units : "))   # Take electricity units from user
total_bill = 0                             # Initialize total bill amount

if (units > 0):                            # Check if units are positive
    if (units > 50):                       # If units are more than 50
        if (units > 150):                  # If units are more than 150
            if (units >= 151):             # If units are 151 or more
                if (units > 250):          # If units exceed 250
                    print("something wrong")  # Invalid condition message
                else:
                    total_bill = 100 * 1.20    # Calculate cost for first 100 units
                    unit4 = units - 100        # Remaining units after 100
                    total_bill = total_bill + (units * 1.50)  # Add cost of remaining units
            else:
                total_bill = 100 * 0.75    # Cost for first 100 units
                unit3 = units - 100        # Remaining units after 100
                total_bill = total_bill + (units * 1.20)  # Add cost for next units
        else:
            total_bill = 50 * 0.5          # Cost for first 50 units
            unit2 = units - 50             # Remaining units after 50
            total_bill = total_bill + (units * 0.75)  # Add cost for remaining units
    else:
        total_bill = units * 0.5           # If units are 50 or less, calculate directly
else:
    print("Invalid input.")                # If units are zero or negative

# Add 20% surcharge
surcharge = total_bill * 0.20              # Calculate 20% surcharge
total_bills = total_bill + surcharge       # Add surcharge to bill

print("Electricity Bill: ₹", round(total_bill, 2))  # Display final bill amount

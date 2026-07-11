# Convert distant given in feet and inches into meter and centimeter.
feet = int(input("Enter the feet: "))
inches = int(input("Enter the inches: "))
totalInches = (feet * 12) + inches    # 1 feet = 12 inches
totalCentimeter = totalInches * 2.54   # 1 inch = 2.54 centimeter
meter = totalCentimeter // 100         # 1 meter = 100 centimeter
centimeter = totalCentimeter % 100     # remaining centimeter
print(f'Meter: {meter}, Centimeter: {centimeter}')

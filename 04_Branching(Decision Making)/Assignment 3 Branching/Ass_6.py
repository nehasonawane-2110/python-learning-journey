# write a program to calculate the profit and loss
# formula
# Profit = Selling Price − Cost Price
# Loss = Cost Price − Selling Price

costPrice = float(input("Enter the cost price: "))
sellingPrice = float(input("Enter the selling price: "))

if (sellingPrice > costPrice):  # profit condition
    print("Profit is", sellingPrice - costPrice)
elif (costPrice > sellingPrice):   # Loss condition
    print("Loss is", costPrice - sellingPrice)
else:                             # no profit and no loss condition
    print("No profit no loss")

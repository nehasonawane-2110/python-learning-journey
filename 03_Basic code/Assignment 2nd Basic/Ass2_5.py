# WAP to calculate selling price of book based on cost price and discount.
costPrice = float(input("Enter the cost price of book: "))
discount = float(input("Enter the discount percentage: "))
sellingPrice = costPrice - (discount / 100) * costPrice
print(f'Selling price of the book is : {sellingPrice}')

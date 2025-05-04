#week 3 assignment
def calculate_discount(price, discount_percentage):


    if discount_percentage >= 0.2:
        price =(1-discount_percentage) * price
    return price

result = calculate_discount(200, 0.2)
print(result) # 160.0
# Get user input for price and discount percentage
price = float(input("Enter the price of the item: "))
discount_percentage = float(input("Enter the discount percentage (0-1): "))
print("The final price after discount is: ", calculate_discount(price, discount_percentage))
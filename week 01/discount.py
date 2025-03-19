from datetime import datetime

# Constants
DISCOUNT_RATE = 0.10
SALES_TAX_RATE = 0.06
DISCOUNT_THRESHOLD = 50

# Get the current day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
current_day= datetime.now().weekday()

# Initialize subtotal
subtotal = 0.0

# Loop to get item prices and quantities until the user enters 0 for price
while True:
    price = float(input("Enter the price of the item or 0 to finish: "))
    if price == 0:
        break
    quantity = int(input("Enter the quantity of the item: "))
    subtotal += price * quantity

# Determine if discount applies
discount = 0
 # Tuesday or Wednesday
if subtotal >= DISCOUNT_THRESHOLD and (current_day == 1 or current_day == 2):
    discount = subtotal * DISCOUNT_RATE
    subtotal -= discount
    print(f"Discount applied: ${discount:.2f}")

# If today is Tuesday or Wednesday but subtotal is below threshold, show how much more is needed
elif current_day == 1 or current_day ==2:
    
    amount_needed = DISCOUNT_THRESHOLD - subtotal
    print(f"Spend ${amount_needed:.2f} more to get a 10% discount!")

# Calculate sales tax and total amount due
Sales_tax = subtotal * SALES_TAX_RATE
total = subtotal + Sales_tax


# Print results
print(f"Sales tax: ${Sales_tax:.2f}")
print(f"Total amount due: ${total:.2f}")
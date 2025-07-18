"""A program to create a meal price calculator for a resturant"""


price = {}
price['children_meal'] = float(
    input("What is the price of a children's meal: "))
price['adult_meal'] = float(input("What is the price of a adult's meal: "))

numbers = []
numbers.append(int(input("How many children are there: ")))
numbers.append(int(input("How many adults are there: ")))

subtotal = (numbers[0] * price['children_meal']) + \
    (numbers[1] * price['adult_meal'])
print(f"Subtotal: #{subtotal:.2f}")


sales_tax_rate = float(input("\nWhat is the sales tax rate: "))
sales_tax = subtotal * (sales_tax_rate / 100)
print(f"Sales Tax: #{sales_tax:.2f}")
total = subtotal + sales_tax
print(f"Total: #{total:.2f}")

payment_amount = float(input("\nWhat is the payment amount: "))
change = payment_amount - total
print(f"Change: #{change:.2f}")
print("\nThank you for your patronage.")

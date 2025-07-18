"""A program to create a meal price calculator for a resturant"""


def get_float(prompt):
    """Function setting while loop."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_int(prompt):
    """Function setting while loop."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.")


price = {}
price['children_meal'] = get_float("What is the price of a children's meal: ")
price['adult_meal'] = get_float("What is the price of a adult's meal: ")

numbers = []
numbers.append(get_int("How many children are there: "))
numbers.append(get_int("How many adults are there: "))

subtotal = (numbers[0] * price['children_meal']) + \
    (numbers[1] * price['adult_meal'])
print(f"\nSubtotal: ${subtotal:.2f}")


sales_tax_rate = get_float("\nWhat is the sales tax rate: ")
sales_tax = subtotal * (sales_tax_rate / 100)
print(f"Sales Tax: ${sales_tax:.2f}")
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")

payment_amount = get_float("\nWhat is the payment amount: ")
change = payment_amount - total
print(f"Change: #{change:.2f}")
print("\nThank you for your patronage.")

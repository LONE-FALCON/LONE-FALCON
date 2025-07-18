number = 0

while number <= 0:
    number = int(input("Please type a positive number: "))
    print("Sorry, that is a negative number. Please try again")

print(f"The number is {number}.")


user_answer = ""

while user_answer != "yes":
    user_answer = input("May I have a piece of candy? (yes/no): ").lower()
print("Thank you!")

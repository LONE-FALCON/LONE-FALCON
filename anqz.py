"""A program that compare strings and numbers."""


first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if first_number > second_number:
    print("The first number is greater")
else:
    print("The first number is not greater")
if first_number == second_number:
    print("The numbers are equal")
else:
    print("The numbers are not equal")
if second_number > first_number:
    print("The second number is greater")
else:
    print("The second number is not greater")

favourite_animal = {}
favourite_animal['Programmer'] = "Falcon"
favourite_animal['User'] = input("What is your favourite animal? ")

if favourite_animal['User'].title() != favourite_animal['Programmer']:
    print("That one is not my favourite.")
else:
    print("That's my favourite animal too!")

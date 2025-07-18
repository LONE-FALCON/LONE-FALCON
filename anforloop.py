"""A program that asks the user for their favorite letter."""

favourite_letter = input("What is your favourite letter? ")
word = "commitment"


for letter in word:
    if letter.lower() == favourite_letter:
        print("_", end="")
    else:
        print(letter.lower(), end="")

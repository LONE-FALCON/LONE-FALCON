"""A simple number guessing game."""

import random


def get_int(prompt):
    """Function setting while loop."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


while True:
    number = random.randint(1, 100)
    count = 0

    while True:
        guess = get_int("What is your guess? ")
        count += 1
        if guess == number:
            print("You guessed it!")
            break
        if guess > number:
            print("Lower.")
        else:
            print("Higher.")
    print(f"It took you {count} guesses.")
    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again != "yes":
        print("\nThank you for playing. Goodbye")
        break

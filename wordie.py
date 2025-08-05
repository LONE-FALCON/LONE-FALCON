"""A simple word guessing game"""

import random


words = ["python", "program", "computer", "challenge",
         "developer", "keyboard", "variable", "function"]
secret_word = random.choice(words)
secret_word_len = len(secret_word)

ATTEMPTS = 6

print("Welcome to Word Guessing Game!")
print(
    f"I am thinking of a word with {secret_word_len} letters. You have {ATTEMPTS} guesses")

INITIAL_HINT = ""
for _ in range(secret_word_len):
    INITIAL_HINT += '_ '
print("\n" + INITIAL_HINT.strip())

while ATTEMPTS > 0:
    guess = input("What is your guess? ").lower()

    if len(guess) != secret_word_len or not guess.isalpha():
        print(
            f"Your guess must be {secret_word_len} letters alphabetic word. Please try again.")
        continue

    if guess == secret_word:
        print(f"\nCongratulations you guessed the word: {secret_word.upper()}")
        break

    HINT = ""
    for i in range(secret_word_len):
        if guess[i] == secret_word[i]:
            HINT += guess[i].upper() + ""
        elif guess[i] in secret_word:
            HINT += guess[i].lower() + ""
        else:
            HINT += '_'
    print(f"Hint: {HINT.strip()}")

    ATTEMPTS -= 1
    print(f"You have {ATTEMPTS} attempts left")

else:
    print(
        f"\nGame Over! You ran out of attempts. The word was {secret_word.strip().upper()}")

"""A program for an adventure game."""


def get_choice(prompt):
    """Function to get a valid choice input."""
    while True:
        try:
            choice = input(prompt).lower()
            if choice in ['']:
                return choice
        except ValueError:
            print("Please enter a valid choice.")


def main():
    """Main function to run the adventure game."""
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. You can go 'left' or 'right'.")

    choice = get_choice("Which way do you want to go? (left/right): ")

    if choice == 'left':
        print("You encounter a wild beast! Game over.")
    elif choice == 'right':
        print("You find a treasure chest! You win!")
    else:
        print("Invalid choice. Please try again.")
        main()
        if __name__ == "__main__":
            main()

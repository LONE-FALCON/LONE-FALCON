# A program that displays a story with  a user's words inserted into the appropriate places(A Mad Lib).

words = {}  # For creating a dictionary.
words['adjective'] = input("\nEnter any adjective of your choice: ")
words['animal'] = input("\nEnter any animal of your choice: ")
words['exclamation'] = input("\nEnter any exclamation remark of your choice: ")
# To capitalize the first letter of the exclamation remark.
user_words = words['exclamation'].capitalize()
words['verb1'] = input("\nEnter any verb1 of your choice: ")
words['verb2'] = input("\nEnter any verb2 of your choice: ")
words['verb3'] = input("\nEnter any verb3 of your choice: ")


# To enter the story


print("\nYour story: ")
story = f'The other day, I was really in trouble. \nIt  all started when I saw a very {words['adjective']} {words['animal']}\
    {words['verb1']} down the hallway. \n{user_words}! I yelled. \nBut all I could do was to {words['verb2']} over and over. \
        \nMiraculously, that caused it to stop, but not before it tried to {words['verb3']} right in front of my family.'
print(story)

"""Assignment on the use of mathematical operations, and conversion of data types in python."""

age = int(input("How old are you? "))
age_next_year = age + 1
print(f"On your next birthday you will be {age_next_year}")

number = int(input("\nHow many egg cartons do you have? "))
eggs = number * 12
print(f"You have {eggs} eggs.")

cookies = int(input("\nHow many cookies do you  have? "))
people = int(input("How many people are there? "))
cookies_per_person = int(cookies / people)
print(f"Each person may have {cookies_per_person} cookies.")

"""A program that determines the letter grade for a course"""


def get_scores(prompt):
    """Function to get a valid score input."""
    while True:
        try:
            user_score = float(input(prompt))
            if 0 <= user_score <= 100:
                return user_score
            print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


score = get_scores("Enter your score: ")
# Define a constant for the passing score
PASSING_SCORE = 70


if score >= 90:
    GRADE = "A"
elif score >= 80:
    GRADE = "B"
elif score >= 70:
    GRADE = "C"
elif score >= 60:
    GRADE = "D"
else:
    GRADE = "F"


# Determine the sign for the grade
if GRADE not in ["A", "F"]:
    last_digit = score % 10
    if last_digit >= 7:
        SIGN = '+'
    elif last_digit < 3:
        SIGN = '-'
    else:
        SIGN = ''
else:
    SIGN = ''

GRADE = GRADE + SIGN
print(f"Your grade is {GRADE}")

if score >= PASSING_SCORE:
    print("You have passed the course.")
else:
    print("You have failed the course.")

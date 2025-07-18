"""A program to compute the areas of three different shapes: a square, a rectangle, and a circle"""


import math


def get_int(prompt):
    """Function setting while loop"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number")


length_of_square = get_int("What is the length of a side of the square? ")
area_of_square = length_of_square ** 2
print(f"The Area of the Square is {area_of_square} cm squared.")


length_of_rectangle = get_int("What is the length of the rectangle? ")
width_of_rectangle = get_int("What is the width of the rectangle? ")
area_of_rectangle = length_of_rectangle * width_of_rectangle
print(f"The Area of the Rectangle is {area_of_rectangle} cm squared.")


radius_of_circle = get_int("What is the radius of the circle? ")
area_of_circle = math.pi * radius_of_circle ** 2
print(f"The area of the Circle is {area_of_circle:.2f} cm squared.")

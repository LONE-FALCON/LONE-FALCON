# program  to print Odd  and  Even numbers

numbers = []
odd_count = 1
even_count = 1

print("Please enter 10 integers. We need  5 odd numbers and 5 even  numbers.")

while len(numbers) < 10:
    num = int(input("Enter a Odd or even number"))

    if num % 2 == 1:
        if odd_count <= 5:
            odd_count += 1
            numbers.append(num)
        else:
            print("you already enter  5 odd numbers")
    elif num % 2 == 0:
        if even_count <= 5:
            even_count += 1
            numbers.append(num)
        else:
            print("you already enter  5 even numbers")
    else:
        print("you must enter a  number")

print(numbers)

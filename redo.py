# A program to input 10 numbers, 5 odd 5 even.

numbers = []
even_count = 1
odd_count = 1

print("Please enter 10 integers. We need 5 even numbers and 5 odd numbers.")

while len(numbers) < 10:
    num = int(input("Enter an even or odd number:"))

    if num % 2 == 0:
        if even_count <= 5:
            even_count += 1
            numbers.append(num)
        else:
            print(
                "You have already entered 5 even numbbers. You need to enter an odd number.")
    elif num % 2 == 1:
        if odd_count <= 5:
            odd_count += 1
            numbers.append(num)
        else:
            print(
                "You have already entered 5 odd numbbers. You need to enter an even number")
    else:
        print("You must enter a number.")

print("\nAll 10 numbers have been entered")
print(f"Entered numbers: {numbers}")

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 == 1]

print(f"Even Numbers: {even_numbers}")
print(f"Odd Numbers: {odd_numbers}")

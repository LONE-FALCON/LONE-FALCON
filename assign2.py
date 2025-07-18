"""A program  to convert temperature from Fahrenheit to Celsius."""

temperature_in_fahrenheit = int(
    input("What is the temperature in Fahrenheit? "))
convert_to_celsius = (temperature_in_fahrenheit - 32) * 5 / 9
print(f"The temperature in Celsius is {convert_to_celsius:.1f} degrees.")

# This program asks for your name and age, then tells you when you'll turn 100.

# Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Calculate the year when the user will turn 100
current_year = 2025
year_turn_100 = current_year + (100 - age)

# Display the result
print(f"Hello, {name}! You will turn 100 years old in the year {year_turn_100}.")

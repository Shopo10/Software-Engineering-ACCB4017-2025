# The volume of a square-based pyramid is calculated using the formula:
#
#
#
# Task:
#
# Write a program to calculate the volume using the above formula.
#
# Allow the user to enter the measurements for a and h. Both a and h should be positive numbers.
#
# Print the volume on the screen to 2 decimal places

# Program to calculate the volume of a square-based pyramid

# Get the base side length (a) from the user
while True:
    try:
        a = float(input("Enter the length of the base side (a): "))
        if a <= 0:
            print("The base side length must be a positive number. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

# Get the height (h) from the user
while True:
    try:
        h = float(input("Enter the height of the pyramid (h): "))
        if h <= 0:
            print("The height must be a positive number. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

# Calculate the volume using the formula V = (a²)h/3
volume = (a ** 2 * h) / 3

# Print the result formatted to 2 decimal places
print(f"The volume of the pyramid is: {volume:.2f}")

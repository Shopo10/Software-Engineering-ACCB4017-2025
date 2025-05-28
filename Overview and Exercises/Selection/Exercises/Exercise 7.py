# Exercises 7

# Ask the user to enter three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Store the numbers in a list
numbers = [num1, num2, num3]

# Sort the list in descending order (biggest to smallest)
numbers.sort(reverse=True)

# Display the numbers
print("Numbers from biggest to smallest:", numbers)


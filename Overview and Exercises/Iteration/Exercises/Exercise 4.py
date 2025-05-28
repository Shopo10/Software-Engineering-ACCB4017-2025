# Exercise 4

# Ask the user for the height
height = int(input("Enter the height of the rectangle: "))

# Fixed width
width = 5

# Draw the rectangle
for _ in range(height):
    print("X" * width)

# Display the summary message
print(f"A {width} x {height} rectangle has been drawn")

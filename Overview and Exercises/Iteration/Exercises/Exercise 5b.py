# Exercise 5b

# Ask the user for dimensions
width = int(input("Enter width of rectangle: "))
height = int(input("Enter height of rectangle: "))

# Draw the rectangle
for _ in range(height):
    for _ in range(width):
        print('X', end="", flush=True)
    print("")  # Move to the next line using print("")

# Final message
print(f"A {width} x {height} rectangle has been drawn")

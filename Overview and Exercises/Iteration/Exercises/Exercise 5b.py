# Exercise 5b

# Ask the user for dimensions
width = int(input("Enter width of rectangle: "))
height = int(input("Enter height of rectangle: "))
name = input("Enter a name to place in the center: ")

# Ensure the name fits inside the rectangle
if len(name) > width - 2:
    print("Error: Name is too long to fit inside the rectangle.")
else:
    middle_row = height // 2

    for row in range(height):
        if row == 0 or row == height - 1:
            print('X' * width)
        elif row == middle_row:
            spaces_on_each_side = (width - 2 - len(name)) // 2
            extra_space = (width - 2 - len(name)) % 2  # Handles odd spacing
            print('X' + ' ' * spaces_on_each_side + name + ' ' * (spaces_on_each_side + extra_space) + 'X')
        else:
            print('X' + ' ' * (width - 2) + 'X')

    # Final message
    print(f"A {width} x {height} hollow rectangle with '{name}' in the center has been drawn.")


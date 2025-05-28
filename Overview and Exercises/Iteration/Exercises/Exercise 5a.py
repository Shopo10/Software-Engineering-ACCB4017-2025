# Exercise 5a

# Ask the user for the line length
length = int(input("Enter length of the line: "))

# Print each 'X' separately
for _ in range(length):
    print('X', end="", flush=True)

# Print the message on a new line
print(f"\nA line of length {length} has been displayed")



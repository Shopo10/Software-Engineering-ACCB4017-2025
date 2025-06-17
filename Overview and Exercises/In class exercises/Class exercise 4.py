#q1

# Get input from the user
user_input = input("Enter a string: ")

# Create lists of all letters and digits
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
digits = list("0123456789")

# Initialize counters
letter_count = 0
number_count = 0

# Loop through each character in the string
for char in user_input:
    if char in letters:
        letter_count += 1
    elif char in digits:
        number_count += 1

# Output the results
print("Number of letters:", letter_count)
print("Number of numbers:", number_count)


print('------------------')

#q2

# Get input from the user
user_input = input("Enter a list of items separated by commas: ")

# Create an empty list to hold each item
items = []
current_item = ""

# Go through each character in the input
for char in user_input:
    if char == ',':
        items.append(current_item)  # Add the current item to the list
        current_item = ""           # Reset for the next item
    else:
        current_item += char        # Add character to the current item

# Add the last item after the loop
items.append(current_item)

# Output each item on a new line
for item in items:
    print(item)

#q3

# Get input from the user
user_input = input("Enter a list of words separated by spaces: ")

# Build the list of words manually without using .split()
words = []
current_word = ""
for char in user_input:
    if char == ' ':
        words.append(current_word)
        current_word = ""
    else:
        current_word += char
# Add the last word
words.append(current_word)

# List of vowels (both lowercase and uppercase)
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# Vowel counters
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

# Go through each word in the list
for word_index in range(len(words)):
    for char_index in range(len(words[word_index])):
        char = words[word_index][char_index]
        if char == 'a' or char == 'A':
            a_count += 1
        elif char == 'e' or char == 'E':
            e_count += 1
        elif char == 'i' or char == 'I':
            i_count += 1
        elif char == 'o' or char == 'O':
            o_count += 1
        elif char == 'u' or char == 'U':
            u_count += 1

# Output the vowel counts
print("a:", a_count)
print("e:", e_count)
print("i:", i_count)
print("o:", o_count)
print("u:", u_count)

#q4
# Empty list to store the numbers
numbers = []

# Instruction to user
print("Enter numbers one by one. Type 'done' to finish.")

# Get input until user types 'done'
while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    else:
        numbers.append(user_input)

# Unique numbers list
unique_numbers = []

# Count how many times each number appears
for i in range(len(numbers)):
    number = numbers[i]
    found = False
    # Check if we've already counted this number
    for j in range(len(unique_numbers)):
        if number == unique_numbers[j]:
            found = True
            break
    # If not found, count it now
    if not found:
        count = 0
        for k in range(len(numbers)):
            if numbers[k] == number:
                count += 1
        print(number + " appears " + str(count) + " time(s).")
        unique_numbers.append(number)

#Advanced exercise
# Empty list to store the numbers
numbers = []

# Get numbers from the user

print("Enter numbers one at a time. Type 'done' to finish.")
#1
while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    else:
        numbers.append(int(user_input))  # Convert to integer when storing

# Manual sorting using selection sort
for i in range(len(numbers)):
    min_index = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j
    # Swap current index with minimum found
    temp = numbers[i]
    numbers[i] = numbers[min_index]
    numbers[min_index] = temp

# Output sorted numbers
print("Numbers in ascending order:")
for i in range(len(numbers)):
    print(numbers[i])

#Very advanced exercises

#exercise 1
def is_prime(n):
    """Check if a number is prime."""
    # Handle special cases
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd numbers up to the square root of n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_squared_primes(numbers):
    """
    Take a list of integers and return a new list containing
    only the prime numbers squared.
    """
    return [num * num for num in numbers if is_prime(num)]


# Test the function
def main():
    # Get input from user
    print("Enter integers (press Enter without input to finish):")
    numbers = []

    while True:
        user_input = input("Enter a number: ").strip()
        if user_input == "":
            break

        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input! Please enter an integer.")

    # Process the numbers and display results
    if numbers:
        result = get_squared_primes(numbers)
        print("\nOriginal numbers:", numbers)
        print("Prime numbers squared:", result)

        # Additional information for clarity
        primes = [num for num in numbers if is_prime(num)]
        print("\nDetailed breakdown:")
        print(f"Prime numbers found: {primes}")
        print(f"Their squares: {result}")
    else:
        print("No numbers were entered!")


if __name__ == "__main__":
    main()
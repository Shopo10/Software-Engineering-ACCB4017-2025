# Write a function called enterphone() which will allow the user to enter a UK mobile phone number and then return it to the main program. The function should also check that the number is a maximum of 13 digits long.
#
# From the main program, call your enterphone() function 3 times, and print the mobile phone numbers returned on the screen.
#
# Also calculate the total cost of the call plans (£12.99 per number)

def enterphone():
    while True:
        phone = input("Enter a UK mobile phone number: ")

        # Remove any spaces from the input
        phone = phone.replace(" ", "")

        # Check if the number starts with proper UK mobile prefix and has correct length
        if phone.startswith("+44"):
            if len(phone) != 13:
                print("Invalid number length. UK mobile numbers should be 13 digits with +44 prefix.")
                continue
        elif phone.startswith("07"):
            if len(phone) != 11:
                print("Invalid number length. UK mobile numbers should be 11 digits when starting with 07.")
                continue
        else:
            print("Invalid UK mobile number. Should start with +44 or 07.")
            continue

        # If we get here, the number is valid
        return phone


# Main program
print("Enter 3 UK mobile phone numbers:")
print("(Valid formats: +447123456789 or 07123456789)")

# Call enterphone() three times and store the numbers
numbers = []
for i in range(3):
    print(f"\nEnter mobile number {i + 1}:")
    number = enterphone()
    numbers.append(number)

# Print all entered numbers
print("\nEntered mobile numbers:")
for i, number in enumerate(numbers, 1):
    print(f"Number {i}: {number}")

# Calculate total cost
cost_per_plan = 12.99
total_cost = cost_per_plan * len(numbers)

# Print the total cost
print(f"\nCost calculation:")
print(f"Number of plans: {len(numbers)}")
print(f"Cost per plan: £{cost_per_plan:.2f}")
print(f"Total cost: £{total_cost:.2f}")
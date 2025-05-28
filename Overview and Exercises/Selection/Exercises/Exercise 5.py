# Exercises 5

# Ask the user to enter their age
age = int(input("Enter your age to book the extreme sports holiday: "))

# Check if the age is within the allowed range
if 18 <= age <= 35:
    print("Booking accepted. You are eligible for the extreme sports holiday!")
else:
    print("Booking rejected. You must be between 18 and 35 years old.")

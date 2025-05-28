# Exercise 2

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print(f"The result is: {result}")
    except ValueError:
        print("Please enter valid numbers.")
        continue

    again = input("Do you want to add two more numbers? Type 'no' to stop: ")
    if again.lower() == "no":
        print("Goodbye!")
        break

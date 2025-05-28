# Exercises 3

# Start the conversation
print("Hello")

# Ask for the user's name
name = input("What is your name? ")
print(f"Hello {name}")

# Ask for the user's age
age = input("What is your age? ")
print(f"Hello {name}, you are {age}")

# Ask how they are feeling
feeling = input("How are you feeling? ").lower()

# Respond based on how they are feeling
if feeling == "good" or feeling == "great" or feeling == "well" or feeling == "happy":
    print(f"That's great to hear, {name}!")
    reason = input("What's making you feel so good? ")
    print(f"Awesome! I'm glad {reason} is making you feel good.")
    future = input("Do you have any plans for the rest of the day? ")
    print(f"That sounds exciting! Enjoy your day, {name}!")
else:
    print(f"I'm sorry to hear that you're feeling {feeling}, {name}.")
    duration = input(f"How long have you been feeling {feeling}? ")
    print(f"That sounds tough. You've been feeling {feeling} for {duration}. I hope things start getting better soon.")
    support = input("Is there anything that helps you feel better? ")
    print(f"It's good to know that {support} helps. Take care, {name}!")



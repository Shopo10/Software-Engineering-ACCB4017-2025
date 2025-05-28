# Exercises 4b

# Player 1 enters their age
age_player1 = int(input("Player 1, enter your age: "))

# Clear the screen (optional, for fairness if you run in a terminal)
print("\n" * 50)

# Player 2 tries to guess the age
guess = int(input("Player 2, guess Player 1's age: "))

# Check the guess
if guess == age_player1:
    print("Correct! You win!")
else:
    difference = abs(guess - age_player1)
    if difference <= 5:
        print("Wrong, but you're warm!")
    else:
        print("Wrong and you're cold!")

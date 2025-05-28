# Exercises 4a

# Player 1 enters their age
age_player1 = int(input("Player 1, enter your age: "))

# Player 2 tries to guess the age
guess = int(input("Player 2, guess Player 1's age: "))

# Check if the guess is correct
if guess == age_player1:
    print("Correct! You win!")
else:
    print("Wrong! You lose.")



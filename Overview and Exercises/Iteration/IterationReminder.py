
#q1
# Get two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Determine the direction of counting
if num1 <= num2:
    # Count up from num1 to num2
    for i in range(num1, num2 + 1):
        print(i, end=' ')
else:
    # Count down from num1 to num2
    for i in range(num1, num2 - 1, -1):
        print(i, end=' ')


#q2
import random

# Get the number of coin flips from the user
num_flips = int(input("How many times would you like to flip the coin? "))

# Initialize counters for heads and tails
heads_count = 0
tails_count = 0

# Perform the coin flips and display results
print("\nFlip results:")
for flip in range(num_flips):
    # Randomly choose between heads (1) and tails (0)
    result = random.choice(['Heads', 'Tails'])
    print(f"Flip {flip + 1}: {result}")

    # Update counters
    if result == 'Heads':
        heads_count += 1
    else:
        tails_count += 1

# Display the final totals
print(f"\nFinal Results:")
print(f"Total flips: {num_flips}")
print(f"Heads: {heads_count}")
print(f"Tails: {tails_count}")

#q3
import random


def play_game():
    # Generate random number between 0 and 100
    target_number = random.randint(0, 100)
    guesses = 0

    print("\nI've thought of a number between 0 and 100!")

    while True:
        # Get user's guess
        try:
            guess = int(input("\nEnter your guess: "))
            guesses += 1

            # Check if guess is correct
            if guess == target_number:
                print(
                    f"\nCongratulations! You've guessed the number in {guesses} {'guess' if guesses == 1 else 'guesses'}!")
                break

            # Calculate distance and give hint
            distance = abs(target_number - guess)

            if distance > 10:
                print("Cold")
            elif distance >= 5:
                print("Warm")
            else:
                print("Hot")

        except ValueError:
            print("Please enter a valid number!")
            continue


def main():
    while True:
        play_game()

        # Ask if player wants to play again
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes' and play_again != 'y':
            print("\nThanks for playing! Goodbye!")
            break


# Start the game
main()
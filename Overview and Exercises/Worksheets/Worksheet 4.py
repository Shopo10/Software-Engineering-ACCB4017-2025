import random


def generate_treasure_locations():
    treasure_locations = random.sample(range(1, 51), 5)
    # Validate that we have 5 unique numbers
    if len(set(treasure_locations)) != 5:
        raise ValueError("Generated treasure locations contain duplicates")
    # Validate that all numbers are within range
    if not all(1 <= x <= 50 for x in treasure_locations):
        raise ValueError("Generated numbers outside valid range (1-50)")
    return treasure_locations

def get_distance_message(distance):
    if distance == 0:
        return "💰 TREASURE FOUND! You've struck gold! 1000 coins!"
    elif 1 <= distance <= 2:
        return "🔥 BURNING HOT! The treasure is practically beneath your feet!"
    elif 3 <= distance <= 4:
        return "♨️ Very Hot! Your metal detector is beeping rapidly!"
    elif 5 <= distance <= 7:
        return "🌡️ Hot! You can sense something valuable nearby!"
    elif 8 <= distance <= 12:
        return "😊 Warm! You're on the right track!"
    elif 13 <= distance <= 18:
        return "😐 Cool! You might want to try elsewhere!"
    elif 19 <= distance <= 25:
        return "🥶 Cold! You're quite far from any treasure!"
    else:
        return "🧊 Freezing! You're nowhere near any treasure!"


def display_game_status(found_treasures, total_coins):
    print("\n" + "=" * 50)
    print(f"Treasures found: {len(found_treasures)}/5")
    print(f"Total coins: {total_coins}")
    if found_treasures:
        print("Found treasure locations:", sorted(found_treasures))
    print("=" * 50)


def play_single_game(treasure_locations):
    print("\n🏴‍☠️ Welcome to Treasure Island! 🏴‍☠️")
    print("There are 5 treasure chests hidden across the island (locations 1-50)")

    found_treasures = []
    total_coins = 0
    attempts = 0

    while len(found_treasures) < 5:
        attempts += 1
        display_game_status(found_treasures, total_coins)

        try:
            guess = int(input("\nWhere would you like to search? "))

            # Input validation
            if guess < 1 or guess > 50:
                print("Please enter a number between 1 and 50!")
                continue

            # Check if location was already searched
            if guess in found_treasures:
                print("You've already found treasure at this location! Try somewhere else!")
                continue

            # Check if the guess is a treasure location
            if guess in treasure_locations:
                print("💰 TREASURE FOUND! You've struck gold! 1000 coins!")
                found_treasures.append(guess)
                total_coins += 1000
                if len(found_treasures) < 5:
                    print(
                        f"Great job! {5 - len(found_treasures)} treasure{'s' if len(found_treasures) < 4 else ''} left to find!")
                else:
                    print("\n🎉 CONGRATULATIONS! You've found all the treasures! 🎉")
                    print(f"Total attempts: {attempts}")
                    print(f"Final score: {total_coins} coins")
            else:
                # Calculate distances only to unfound treasures
                remaining_treasures = [loc for loc in treasure_locations if loc not in found_treasures]
                if remaining_treasures:  # Only calculate distances if there are unfound treasures
                    min_distance = min(abs(guess - loc) for loc in remaining_treasures)
                    message = get_distance_message(min_distance)
                    print(message)

                    if min_distance <= 2:
                        print(f"(You're only {min_distance} locations away from an unfound treasure!)")
                    elif min_distance > 2:
                        print("Try searching in a different area of the island!")

        except ValueError:
            print("Please enter a valid number!")


def main():
    playing = True
    while playing:
        # Generate new treasure locations for each game
        treasure_locations = generate_treasure_locations()

        # Play a single game
        play_single_game(treasure_locations)

        # Ask if they want to play again
        while True:
            play_again = input("\nWould you like to start a new treasure hunt? (yes/no): ").lower()
            if play_again in ['yes', 'no']:
                break
            print("Please answer with 'yes' or 'no'")

        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            playing = False


# Start the game
if __name__ == "__main__":
    main()
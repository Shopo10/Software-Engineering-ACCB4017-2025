import random


def generate_treasure_locations():
    return random.sample(range(1, 51), 5)


def display_game_status(found_treasures, total_coins):
    print("\n" + "=" * 50)
    print(f"Treasures found: {len(found_treasures)}/5")
    print(f"Total coins: {total_coins}")
    if found_treasures:
        print("Found treasure locations:", sorted(found_treasures))
    print("=" * 50)


def shuffle_remaining_treasures(treasure_locations, found_treasures):
    # Get all possible locations (1-50) excluding found treasure spots
    available_spots = [x for x in range(1, 51) if x not in found_treasures]
    # Count unfound treasures
    treasures_to_place = 5 - len(found_treasures)
    # Generate new locations for unfound treasures
    new_locations = random.sample(available_spots, treasures_to_place)

    # Create new treasure_locations list with found treasures preserved
    new_treasure_locations = found_treasures.copy()
    new_treasure_locations.extend(new_locations)
    return new_treasure_locations


def play_single_game():
    print("\n🏴‍☠️ Welcome to Treasure Island! 🏴‍☠️")
    print("There are 5 treasure chests hidden across the island (locations 1-50)")
    print("⚠️ Warning: The treasures move to new locations after each unsuccessful search!")

    found_treasures = []
    total_coins = 0
    attempts = 0
    treasure_locations = generate_treasure_locations()

    while len(found_treasures) < 5:
        attempts += 1
        display_game_status(found_treasures, total_coins)

        try:
            guess = int(input("\nWhere would you like to search? "))

            # Input validation
            if guess < 1 or guess > 50:
                print("Please enter a number between 1 and 50!")
                continue

            # Check if location was already searched successfully
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
                print("❌ No treasure here! The unfound treasures have moved to new locations!")
                # Shuffle the remaining unfound treasures
                treasure_locations = shuffle_remaining_treasures(treasure_locations, found_treasures)

        except ValueError:
            print("Please enter a valid number!")


def main():
    playing = True
    while playing:
        # Play a single game
        play_single_game()

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
def check_answer(answer):
    # Dictionary of valid answers and their scores
    cities = {
        'cardiff': 91,
        'swansea': 82,
        'newport': 62,
        'st davids': 7,
        'st asaph': 0,
        'wrexham': 0,
        'bangor': 0
    }

    # Convert answer to lowercase for case-insensitive comparison
    answer = answer.lower()

    # Check if the answer is in our dictionary of valid answers
    if answer in cities:
        score = cities[answer]
        if score == 0:
            return score, "Congratulations! That's a Pointless answer!"
        else:
            return score, "Correct answer, but not pointless."
    else:
        return 100, "Wrong answer!"


def play_pointless():
    print("Welcome to Pointless!")
    print("\nIn this game, you need to give correct answers that few people know.")
    print("Wrong answers score 100 points.")
    print("The aim is to score as few points as possible!")
    print("\nLet's begin!")

    print("\nQuestion: Name a city in Wales")

    # Get player's answer
    answer = input("\nYour answer: ")

    # Check the answer and get score
    score, message = check_answer(answer)

    # Display results
    print("\n" + message)
    print(f"You scored {score} points!")

    if score == 0:
        print("Well done! You found a Pointless answer!")
    elif score == 100:
        print("The correct answers were:")
        print("Cardiff (91 points)")
        print("Swansea (82 points)")
        print("Newport (62 points)")
        print("St Davids (7 points)")
        print("St Asaph (0 points)")
        print("Wrexham (0 points)")
        print("Bangor (0 points)")


# Start the game
play_pointless()
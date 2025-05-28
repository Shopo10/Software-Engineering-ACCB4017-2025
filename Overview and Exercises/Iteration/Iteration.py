# Iteration Overview

# for loop
# while loop



numberOfLoops = int(input("Enter a number less than 10 or 0 to exit"))

while numberOfLoops != 0:
    print(f"You entered {numberOfLoops}")
    if numberOfLoops < 10:
        print("Loop")
    else:
        print("STOP!!!!")
    numberOfLoops = (numberOfLoops -1)
    if numberOfLoops == 3:
        break
    print("You found the hidden number")
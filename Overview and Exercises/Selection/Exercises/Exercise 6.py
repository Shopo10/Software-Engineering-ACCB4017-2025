# Exercises 6

# Ask the user to enter the student's score
score = int(input("Enter the student's score: "))

# Determine the mark based on the score
if score > 90:
    mark = 4
elif 80 <= score <= 89:
    mark = 3
elif 70 <= score <= 79:
    mark = 2
elif 60 <= score <= 69:
    mark = 1
else:
    mark = 0

# Display the result
print(f"The student's mark is: {mark}")

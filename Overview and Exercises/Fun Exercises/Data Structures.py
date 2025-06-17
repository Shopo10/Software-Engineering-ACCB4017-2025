#q1
# Create an empty list
values = []
original_values = []  # To store a copy for reverse printing

# Get input values from user
print("Enter values for the list (press Enter without input to finish):")
while True:
    value = input("Enter a value: ")
    if value == "":  # If user presses Enter without input, stop taking values
        break
    values.append(value)
    original_values.append(value)  # Keep a copy of the original values

print("\nPrinting values in original order:")
# Print values using pop(0) until list is empty
while values:
    print(values.pop(0))

print("\nPrinting values in reverse order:")
# Print values using pop() until list is empty
while original_values:
    print(original_values.pop())






#q2

# Create an empty list to store unique integers
numbers = []

print("Enter integers to add to the list (-1 to finish):")

while True:
    # Get input from user
    try:
        num = int(input("Enter a number: "))

        # Check for sentinel value (-1)
        if num == -1:
            break

        # Check if number is already in the list
        if num in numbers:
            print(f"{num} is already in the list! Duplicate not added.")
        else:
            numbers.append(num)
            print(f"{num} added to the list.")

    except ValueError:
        print("Invalid input! Please enter an integer.")

# Output the final list
print("\nFinal list of unique numbers:")
print(numbers)
print(f"Total unique numbers: {len(numbers)}")







#q3
def calculate_grade(average):
    if average >= 70:
        return "1st"
    elif average >= 60:
        return "2:1"
    elif average >= 50:
        return "2:2"
    elif average >= 40:
        return "3rd"
    else:
        return "Fail"


# Initialize empty lists to store student data
students = []
marks = []

print("Student Mark System")
print("Enter student details (press Enter without name to finish)")

while True:
    # Get student name
    name = input("\nEnter student name: ").strip()
    if name == "":
        break

    # Get two marks with validation
    student_marks = []
    for i in range(2):
        while True:
            try:
                mark = float(input(f"Enter mark {i + 1} for {name}: "))
                if 0 <= mark <= 100:
                    student_marks.append(mark)
                    break
                else:
                    print("Mark must be between 0 and 100")
            except ValueError:
                print("Invalid input! Please enter a number")

    # Calculate average for this student
    student_average = sum(student_marks) / len(student_marks)

    # Store student data
    students.append(name)
    marks.append({
        'marks': student_marks,
        'average': student_average,
        'grade': calculate_grade(student_average)
    })

# Print results only if there are students
if students:
    print("\n=== Student Results ===")
    print("\nIndividual Results:")
    print("-" * 50)

    # Track highest and lowest scores
    highest_avg = float('-inf')
    lowest_avg = float('inf')
    highest_student = ""
    lowest_student = ""
    total_average = 0

    # Print individual results and track statistics
    for i in range(len(students)):
        student = students[i]
        student_data = marks[i]

        print(f"Student: {student}")
        print(f"Marks: {student_data['marks'][0]}, {student_data['marks'][1]}")
        print(f"Average: {student_data['average']:.2f}")
        print(f"Grade: {student_data['grade']}")
        print("-" * 50)

        # Update highest/lowest tracking
        if student_data['average'] > highest_avg:
            highest_avg = student_data['average']
            highest_student = student
        if student_data['average'] < lowest_avg:
            lowest_avg = student_data['average']
            lowest_student = student

        total_average += student_data['average']

    # Calculate and print class statistics
    class_average = total_average / len(students)

    print("\n=== Class Statistics ===")
    print(f"Highest performing student: {highest_student} ({highest_avg:.2f}%)")
    print(f"Lowest performing student: {lowest_student} ({lowest_avg:.2f}%)")
    print(f"Class average: {class_average:.2f}%")

else:
    print("\nNo students were entered.")




#q4

def print_menu():
    print("\nQueue Operations:")
    print("1. Push - Add an element to the queue")
    print("2. Pop - Remove and display first element")
    print("3. Print - Display all elements")
    print("4. Exit")


# Initialize an empty queue
queue = []

while True:
    print_menu()
    choice = input("\nEnter your choice (push/pop/print/exit): ").lower().strip()

    if choice == 'push':
        # Add element to the end of queue
        value = input("Enter value to add: ")
        queue.append(value)
        print(f"Added '{value}' to the queue")

    elif choice == 'pop':
        # Remove and display first element if queue is not empty
        if not queue:
            print("Error: Queue is empty! Nothing to pop.")
        else:
            value = queue.pop(0)
            print(f"Popped value: {value}")

    elif choice == 'print':
        # Display all elements in queue
        if not queue:
            print("Queue is empty!")
        else:
            print("\nCurrent queue contents:")
            print("Front →", end=" ")
            for item in queue:
                print(item, end=" → ")
            print("Back")
            print(f"Queue size: {len(queue)}")

    elif choice == 'exit':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please use push/pop/print/exit")
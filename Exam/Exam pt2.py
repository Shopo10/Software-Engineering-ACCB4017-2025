# Declare an empty list in your program to hold some measurements, for example:
#
# rainfall = []
#
# 1. Prompt the user to enter five (valid) rainfall measurements (in millimetres) and store them in a list. (eg 3.3, 5.0, 2.6 etc)
#
# 2. Print each of the entered values on the screen using a loop.
#
# 3. Calculate the total rainfall (ie add all five measurements)
#
# 4. Also calculate the average rainfall and print it on the screen

# Initialize an empty list to store rainfall measurements
rainfall = []

# 1. Get five valid rainfall measurements from the user
print("Please enter five rainfall measurements in millimeters")

while len(rainfall) < 5:
    try:
        measurement = float(input(f"Enter rainfall measurement {len(rainfall) + 1}: "))
        if measurement < 0:
            print("Rainfall cannot be negative. Please enter a valid measurement.")
            continue
        rainfall.append(measurement)
    except ValueError:
        print("Please enter a valid number.")

# 2. Print each measurement using a loop
print("\nYour entered measurements:")
for i, measurement in enumerate(rainfall, 1):
    print(f"Measurement {i}: {measurement} mm")

# 3. Calculate the total rainfall
total_rainfall = sum(rainfall)

# 4. Calculate and print the average rainfall
average_rainfall = total_rainfall / len(rainfall)

# Print the results
print(f"\nTotal rainfall: {total_rainfall} mm")
print(f"Average rainfall: {average_rainfall:.2f} mm")
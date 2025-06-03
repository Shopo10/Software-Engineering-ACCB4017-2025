# Worksheet 1 - The Concept of Variables

# Ask the user for car details and display them with basic input validation

# Get car make from user
car_make = input("Enter the car make (e.g., Toyota): ").strip()

# Get car model from user
car_model = input("Enter the car model (e.g., Corolla): ").strip()

# Get car registration from user (no lowercase letters allowed)
car_registration = input("Enter the car registration (uppercase only): ").strip()
while any(c.islower() for c in car_registration):
    print("Lowercase letters are not allowed.")
    car_registration = input("Enter the car registration (uppercase only): ").strip()

# Get year of production and validate it's a number in a reasonable range
while True:
    year_input = input("Enter the year of production (e.g., 2020): ")
    if year_input.isdigit():
        car_year = int(year_input)
        if 1886 <= car_year <= 2025:  # 1886 = first car invented, 2025 = current/future year
            break
        else:
            print("Please enter a year between 1886 and 2025.")
    else:
        print("Invalid input. Please enter a numeric year.")

# Get fuel type and check it's a known type
valid_fuels = ['petrol', 'diesel', 'electric', 'hybrid']
while True:
    car_fuel_type = input("Enter the fuel type (petrol, diesel, electric, hybrid): ").strip().lower()
    if car_fuel_type in valid_fuels:
        break
    else:
        print("Invalid fuel type. Please choose from petrol, diesel, electric, or hybrid.")

# Get engine size/fuel in liters (e.g., 2.0 for 2.0 L engine)
while True:
    engine_fuel = input("Enter the engine size in liters (e.g., 2.0): ")
    try:
        engine_fuel = float(engine_fuel)
        if 0 < engine_fuel <= 8.0:
            break
        elif engine_fuel <= 0:
            print("Engine size must be a positive number.")
        else:
            print("Engine size cannot exceed 8.0 liters.")
    except ValueError:
        print("Invalid input. Please enter a number (e.g., 1.6, 2.0).")

# Display all collected information
print("\nCar Information:")
print(f"Make: {car_make}")
print(f"Model: {car_model}")
print(f"Registration: {car_registration}")
print(f"Year of Production: {car_year}")
print(f"Fuel Type: {car_fuel_type.capitalize()}")
print(f"Engine Size: {engine_fuel}L")


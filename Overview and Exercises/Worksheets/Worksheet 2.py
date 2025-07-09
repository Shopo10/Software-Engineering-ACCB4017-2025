def get_valid_duration():
    MAX_DURATION = 168  # Hard upper limit (1 week)
    while True:
        try:
            duration = float(input("Enter duration of parking in hours (e.g. 2.5): "))
            if duration <= 0:
                print("Duration must be greater than 0. Try again.")
            elif duration > MAX_DURATION:
                print(f"Duration cannot exceed {MAX_DURATION} hours (1 week). Try again.")
            elif duration < 1 or duration > 72:
                confirmation = input(f"You entered {duration} hours. Are you sure? (yes/no): ").lower()
                if confirmation == "yes":
                    return duration
                else:
                    print("Let's try again.")
            else:
                return duration
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_vehicle_type():
    vehicle_types = {
        "car": "Car",
        "motorcycle": "Motorcycle",
        "van": "Van",
        "ev": "Electric Vehicle",
        "bus": "Bus"
    }
    while True:
        print("\nSelect vehicle type:")
        for code, name in vehicle_types.items():
            print(f" - {code}: {name}")
        choice = input("Enter vehicle type: ").lower()
        if choice in vehicle_types:
            return choice
        else:
            print("Invalid vehicle type. Try again.")

def is_weekend():
    while True:
        response = input("Is this parking on a weekend? (yes/no): ").lower()
        if response in ["yes", "no"]:
            return response == "yes"
        print("Please answer with 'yes' or 'no'.")

def calculate_fee(duration, vehicle, weekend):
    rates = {
        "car":        {"weekday": 2.50, "weekend": 3.00, "max": 15.00},
        "motorcycle": {"weekday": 1.00, "weekend": 1.20, "max": 6.00},
        "van":        {"weekday": 4.00, "weekend": 4.80, "max": 25.00},
        "ev":         {"weekday": 1.80, "weekend": 2.16, "max": 12.00},
        "bus":        {"weekday": 6.00, "weekend": 7.20, "max": 30.00}
    }

    rate_type = "weekend" if weekend else "weekday"
    hourly_rate = rates[vehicle][rate_type]
    daily_max = rates[vehicle]["max"]

    full_days = int(duration) // 24
    remaining_hours = duration % 24

    day_fee = min(remaining_hours * hourly_rate, daily_max)
    total_fee = full_days * daily_max + day_fee

    return round(total_fee, 2)

# Main Program
print("Welcome to the Multi-Storey Car Park Fee Calculator!")

duration = get_valid_duration()
vehicle = get_vehicle_type()
weekend = is_weekend()

fee = calculate_fee(duration, vehicle, weekend)

vehicle_names = {
    "car": "Car",
    "motorcycle": "Motorcycle",
    "van": "Van",
    "ev": "Electric Vehicle",
    "bus": "Bus"
}

print(f"\n--- Receipt ---")
print(f"Vehicle Type: {vehicle_names[vehicle]}")
print(f"Duration: {duration} hours")
print(f"Day Type: {'Weekend' if weekend else 'Weekday'}")
print(f"Total Parking Fee: £{fee:.2f}")

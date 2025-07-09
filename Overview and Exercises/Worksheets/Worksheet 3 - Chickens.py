#Worksheet 3 - Chickens
while True:
    print("\n1. Regular Food\n2. Superfood\n3. Mixed Food\n4. Exit")
    choice = input("Select option (1-4): ")

    if choice == "4":
        break
    if choice not in ["1", "2", "3"]:
        print("Invalid option")
        continue

    try:
        days = int(input("Enter total days: "))
        if days < 0:
            print("Days must be positive")
            continue

        if days > 35:  # Check for egg spoilage
            print("Eggs are bad and cannot be used")
            continue

        if choice == "1":
            eggs = days  # Regular: 1 egg per day
        elif choice == "2":
            eggs = (days // 2 * 3) + (days % 2)  # Superfood: 3 eggs per 2 days
        else:
            super_days = int(input("Enter days on superfood: "))
            if super_days > days:
                print("Superfood days cannot exceed total days")
                continue
            regular_days = days - super_days
            super_eggs = (super_days // 2 * 3) + (super_days % 2)
            regular_eggs = regular_days
            eggs = super_eggs + regular_eggs

        print(f"\nTotal eggs: {eggs}")
        print(f"Possible cakes: {eggs // 2}")
        print(f"Remaining eggs: {eggs % 2}")

    except ValueError:
        print("Invalid number")
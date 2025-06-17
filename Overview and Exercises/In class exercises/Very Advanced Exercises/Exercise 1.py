# Exercise 1

def is_prime(n):
    if n < 2: return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

# Get numbers from user
numbers = []
while True:
    try:
        num = input("Enter a number (or press Enter to finish): ").strip()
        if num == "": break
        numbers.append(int(num))
    except ValueError:
        print("Please enter a valid integer")

# Get squared primes using list comprehension
squared_primes = [n * n for n in numbers if is_prime(n)]

print(f"\nOriginal numbers: {numbers}")
print(f"Prime numbers squared: {squared_primes}")


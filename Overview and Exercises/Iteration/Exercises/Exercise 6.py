# Exercise 6


expressions = [
    ('"12345" + 678910', lambda: "12345" + 678910),
    ('123 + 45.6', lambda: 123 + 45.6),
    # '09 + 11' cannot be run due to SyntaxError, so we skip or demonstrate differently
    ('14 * "1.2"', lambda: 14 * "1.2"),
    ('8 / 2.0', lambda: 8 / 2.0),
    ('"abc" + "def"', lambda: "abc" + "def"),
    ('"ghi" + jkl', lambda: "ghi" + jkl),
    ('5.0 % 3', lambda: 5.0 % 3),
]

for expr, func in expressions:
    try:
        res = func()
        print(f'{expr} => res = {res}')
    except Exception as e:
        print(f'{expr} => Error: {e}')

print("\nNote: Expression '09 + 11' is invalid syntax in Python and cannot be executed.")

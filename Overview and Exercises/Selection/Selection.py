"""Selection and Comparison Operators Overview

Comparison Operators:
==    Equal to
!=    Not equal to
>     Greater than
<     Less than
>=    Greater than or equal to
<=    Less than or equal to
in    Membership operator
is    Identity operator

Logical Operators:
and   Logical AND
or    Logical OR
not   Logical NOT

Example:
if age >= 18 and is_registered:
    print("Eligible to vote")
"""

def determine_barrels():
    print("Pick one sweet from the barrel labeled 'Mixture'")
    sweet = input("What kind of sweet did you get? (Apple or Pear): ").strip().lower()

    if sweet == "apple":
        print("\nCorrect labeling:")
        print("Barrel labeled 'Mixture' contains: Apple")
        print("Barrel labeled 'Pear' contains: Mixture")
        print("Barrel labeled 'Apple' contains: Pear")
    elif sweet == "pear":
        print("\nCorrect labeling:")
        print("Barrel labeled 'Mixture' contains: Pear")
        print("Barrel labeled 'Apple' contains: Mixture")
        print("Barrel labeled 'Pear' contains: Apple")
    else:
        print("Invalid sweet type.")

determine_barrels()
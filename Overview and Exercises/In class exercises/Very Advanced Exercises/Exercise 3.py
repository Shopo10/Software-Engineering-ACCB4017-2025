def get_permutations(lst):
    # Base case
    if len(lst) <= 1:
        yield lst
        return

    # Track used elements to avoid duplicates
    used = set()

    for i in range(len(lst)):
        # Skip if we've already used this element at this position
        if lst[i] not in used:
            used.add(lst[i])
            # Get remaining elements
            rest = lst[:i] + lst[i + 1:]
            # Recursively generate permutations of remaining elements
            for p in get_permutations(rest):
                yield [lst[i]] + p


# Test function
def test_permutations():
    test_list = [1, 1, 2]
    print(f"Original list: {test_list}")
    print("All unique permutations:")
    for i, perm in enumerate(get_permutations(test_list), 1):
        print(f"{i}. {perm}")


if __name__ == "__main__":
    test_permutations()
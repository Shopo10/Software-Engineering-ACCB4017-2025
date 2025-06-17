def intersect_with_frequency(*lists):
    if not lists: return []
    # Count elements in each list and find minimum frequencies
    freq_by_list = [{}]
    for lst in lists:
        counts = {}
        for item in lst:
            counts[item] = counts.get(item, 0) + 1
        freq_by_list.append(counts)

    # Get items that appear in all lists with their minimum frequency
    result = []
    common_elements = set.intersection(*[set(d.keys()) for d in freq_by_list[1:]])
    for item in common_elements:
        min_freq = min(d.get(item, 0) for d in freq_by_list[1:])
        result.extend([item] * min_freq)

    return result


# Test the function
list1 = [1, 1, 2, 2, 3, 3]
list2 = [1, 1, 1, 2, 2, 4]
list3 = [1, 1, 2, 3, 3, 3]

result = intersect_with_frequency(list1, list2, list3)
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"List 3: {list3}")
print(f"Intersection with frequency: {result}")
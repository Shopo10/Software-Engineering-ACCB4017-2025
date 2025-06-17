def lis_recursive(arr):
    n = len(arr)
    memo = {}

    def lis_helper(curr_idx, prev_idx):
        if curr_idx == n:
            return [], 0

        key = (curr_idx, prev_idx)
        if key in memo:
            return memo[key]

        # Don't include current element
        skip_seq, skip_len = lis_helper(curr_idx + 1, prev_idx)

        # Include current element if it maintains increasing order
        take_seq, take_len = [], 0
        if prev_idx == -1 or arr[curr_idx] > arr[prev_idx]:
            next_seq, next_len = lis_helper(curr_idx + 1, curr_idx)
            take_seq = [arr[curr_idx]] + next_seq
            take_len = 1 + next_len

        # Store and return the better result
        if take_len > skip_len:
            memo[key] = (take_seq, take_len)
        else:
            memo[key] = (skip_seq, skip_len)
        return memo[key]

    sequence, length = lis_helper(0, -1)
    return length, sequence


def lis_dp(arr):
    if not arr:
        return 0, []

    n = len(arr)
    # lengths[i] stores length of LIS ending at i
    lengths = [1] * n
    # prev[i] stores previous index in the LIS ending at i
    prev = [-1] * n

    # Best length and its ending index
    best_len = 1
    best_end = 0

    # Fill lengths and prev arrays
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lengths[j] + 1 > lengths[i]:
                lengths[i] = lengths[j] + 1
                prev[i] = j
                if lengths[i] > best_len:
                    best_len = lengths[i]
                    best_end = i

    # Reconstruct the sequence
    sequence = []
    while best_end != -1:
        sequence.insert(0, arr[best_end])
        best_end = prev[best_end]

    return best_len, sequence


# Test both implementations
def test_lis():
    test_cases = [
        [10, 9, 2, 5, 3, 7, 101, 18],
        [0, 1, 0, 3, 2, 3],
        [7, 7, 7, 7],
        [3, 10, 2, 1, 20]
    ]

    for arr in test_cases:
        print(f"\nInput array: {arr}")

        # Test recursive solution
        rec_len, rec_seq = lis_recursive(arr)
        print(f"Recursive - Length: {rec_len}, Sequence: {rec_seq}")

        # Test DP solution
        dp_len, dp_seq = lis_dp(arr)
        print(f"DP       - Length: {dp_len}, Sequence: {dp_seq}")


if __name__ == "__main__":
    test_lis()
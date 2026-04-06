"""
Highest Value Longest Common Subsequence (HVLCS)

Given two strings A and B and character values, finds the common
subsequence that maximizes total character value using dynamic programming.
"""

import sys
import time


def parse_input(filepath):
    """
    Parse an input file with the format:
        K
        x1 v1
        x2 v2
        ...
        xK vK
        A
        B

    Returns:
        char_values (dict): mapping from character to its integer value
        A (str): first string
        B (str): second string
    """
    with open(filepath, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    k = int(lines[0])
    char_values = {}
    for i in range(1, k + 1):
        parts = lines[i].split()
        char = parts[0]
        value = int(parts[1])
        char_values[char] = value

    A = lines[k + 1]
    B = lines[k + 2]

    return char_values, A, B


def solve_hvlcs(char_values, A, B):
    """
    Compute the Highest Value Longest Common Subsequence using DP.

    dp[i][j] = maximum value of a common subsequence of A[0..i-1] and B[0..j-1]

    Recurrence:
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + value(A[i-1])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    Base cases:
        dp[0][j] = 0 for all j (empty prefix of A)
        dp[i][0] = 0 for all i (empty prefix of B)

    Args:
        char_values (dict): character -> integer value
        A (str): first string
        B (str): second string

    Returns:
        max_value (int): the maximum value achievable
        subsequence (str): one optimal common subsequence
    """
    m = len(A)
    n = len(B)

    # Build DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + char_values.get(A[i - 1], 0)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    max_value = dp[m][n]

    # Backtrack to reconstruct one optimal subsequence
    subsequence = []
    i, j = m, n
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            subsequence.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    subsequence.reverse()

    return max_value, ''.join(subsequence)


def main():
    if len(sys.argv) < 2:
        print("Usage: python hvlcs.py <input_file>")
        sys.exit(1)

    filepath = sys.argv[1]

    char_values, A, B = parse_input(filepath)

    start_time = time.time()
    max_value, subsequence = solve_hvlcs(char_values, A, B)
    elapsed = time.time() - start_time

    print(max_value)
    print(subsequence)

    # Print timing info to stderr so it doesn't interfere with output
    print(f"Time: {elapsed:.6f} seconds", file=sys.stderr)


if __name__ == "__main__":
    main()
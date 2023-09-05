#!/usr/bin/python3
#prepare for interview questions
def minOperations(n):
    if n <= 1:
        return 0
    
    # Array to store the minimum operations for each length.
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        # Initialize with the maximum possible value.
        dp[i] = float('inf')
        for j in range(1, i):
            if i % j == 0:
                # If j is a divisor of i, we can create a substring of length j
                # and then repeat it (i // j) times to get a string of length i.
                dp[i] = min(dp[i], dp[j] + i // j)
    
    return dp[n]

# Example usage:
n = 9
result = minOperations(n)
print("Number of operations:", result)  # Output: Number of operations: 6

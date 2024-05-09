#!/usr/bin/python3
def minOperations(n):
    if n <= 0:
        return 0

    # Initialize dp array to store minimum operations to reach each number
    dp = [float('inf')] * (n + 1)

    # Base cases
    dp[1] = 0  # Starting with 1 H, no operations needed

    # Fill the dp array bottom-up
    for i in range(2, n + 1):
        # Try all factors of i to find the minimum operations
        for j in range(1, i):
            if i % j == 0:
                # If j is a factor of i, copy j Hs and paste i/j times to get i Hs
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0
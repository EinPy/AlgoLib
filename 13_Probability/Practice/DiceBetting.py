import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

def probability_of_at_least_k_different_numbers(n, s, k):
    # Initialize the dynamic programming table
    dp = [[0.0 for _ in range(s + 2)] for _ in range(n + 2)]

    # Base case
    dp[0][0] = 1.0

    # Fill the table using dynamic programming
    for i in range(n):
        for j in range(s + 1):
            # Update probability for getting a new unique number in the next throw
            dp[i + 1][j + 1] += dp[i][j] * (s - j) / s
            # Update probability for getting a number we've already seen in the next throw
            dp[i + 1][j] += dp[i][j] * j / s

    # Calculate the probability of throwing at least k different numbers within n throws
    probability = sum(dp[n][j] for j in range(k, s + 1))

    return probability

# Input
n, s, k = nl()

# Calculate probability
prob = probability_of_at_least_k_different_numbers(n, s, k)

# Output
print(f"{prob:.10f}")
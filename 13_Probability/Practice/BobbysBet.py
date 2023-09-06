import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

from math import comb

def probability_of_rolling_r_or_higher(s, r, x, y):
    # Calculate the probability of rolling a score of R or higher at least X times when rolling a dice with S sides Y times in total.
    probability = 0
    for i in range(x, y + 1):
        success = (s - r + 1) / s
        failure = (r - 1) / s
        probability += comb(y, i) * (success ** i) * (failure ** (y - i))

    return probability


t = ni()
for case in range(t):
    R, S, X, Y, W = nl()
    #reach score, sides, X out of Y rolls, multiply
    ans = probability_of_rolling_r_or_higher(S, R, X, Y)
    if ans * W > 1:
        print("yes")
    else:
        print("no")
        
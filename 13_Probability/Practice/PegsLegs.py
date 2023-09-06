import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


def max_expected_score(L, P, legs, pegs):
    expected_values = [0] * (L + P + 1)
    for i in range(L):
        expected_values[i + 1] = legs[i]

    for i in range(P, 0, -1):
        l, r, x, y = pegs[i - 1]
        stuck = 1 - l - r
        expected_values[i + L] = (l * expected_values[x] + r * expected_values[y]) / (1 - stuck)

    drop_points = set(range(1, L + P + 1)) - {x for _, _, x, _ in pegs} - {y for _, _, _, y in pegs}
    max_score = 0
    for i in drop_points:
        max_score = max(max_score, expected_values[i])

    return max_score

L, P = nl()
legs = []
pegs = []
for _ in range(L):
    legs.append(ni())
    
for _ in range(P):
    l, r, x, y = INP().split()
    pegs.append((float(l), float(r), int(x), int(y)))
print(f"{max_expected_score(L, P, legs, pegs):.10f}")
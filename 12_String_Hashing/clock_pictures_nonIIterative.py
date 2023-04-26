import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

MOD = 10**16 + 61
p = 400000

def solve(l, a, b):
    pass

def pref (S):
    #computing prefiix array
    hashes = [0]
    pw = [1]
    for ch in S:
        last = hashes[-1]
        h = (last * p + ch) % MOD
        hashes.append(h)
        pw.append(pw[-1] * p % MOD)
        
def hash(pref, pw, L, R):
    


l = ni()
a, b = nl(), nl()
if solve(l, a, b):
    print("possible")
else:
    print("impossible")
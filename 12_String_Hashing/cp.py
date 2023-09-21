import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    pass


n = ni()
a = nl()
b = nl()
a = a
diff = []
diff[0] = a[0] - a[n-1]
b = b + b

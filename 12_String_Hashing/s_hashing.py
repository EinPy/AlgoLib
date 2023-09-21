import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

MOD = 10**16 + 61
BAS = 10



def ok(s):
    cur = 0
    out = [0]* len(s)
    for i in range(len(s)):
        #print(i, s[i])
        cur = (cur * BAS) % MOD
        cur = (cur + ord(s[i])) % MOD
        out[i] = cur
    return out


s = INP()
#compute prefix 
pref = ok(s)
q = ni()
print(ok("ab"), ok("ba"))
print(pref)
for _ in range(q):
    a, b = nl()
    l = b - a
    b -= 1
    if a == 0:
        print(pref[b])
    else:
        print((pref[b] - pref[a-1] * pow(BAS, l, MOD)) % MOD)

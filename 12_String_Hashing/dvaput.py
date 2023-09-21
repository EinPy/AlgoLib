import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


MOD = 10**16 + 61
BAS = 200



def ok(s, n):
    if n == 0:
        return True
    if n == 1:
        if len(set(list(s))) == len(list(s)):
            return False
        else:
            return True
    cur = 0
    rem = pow(BAS, n-1, MOD)
    seen = {}
    for i in range(n):
        #print(i, s[i])
        cur = (cur * BAS) % MOD
        cur = (cur + ord(s[i])) % MOD
    
    #print(s[:n])
    seen[cur] = True
    #print(cur)
    for i in range(n, len(s) - 1):
        #remove
        cur = (cur - ord(s[i - n]) * (rem)) % MOD
        cur = (cur * BAS + ord(s[i])) % MOD
        
        #print(i, i-n, s[i-n: i], s[i-n], s[i], cur)
        if cur in seen:
            return True
        seen[cur] = True

    return False

#Binary search for higher bound
def high_bound(a):
    l, r,  = 0, len(a)
    ans = -1
    while l < r:
        mid = (l + r) // 2
        #print(l, r, mid, a)
        if ok(a, mid):
            ans = mid
            l = mid+1
        else:
            r = mid
    return ans
        
       
h = ni() 
s = INP()
l = [ord(s[i]) for i in range(len(s))]

print(high_bound(s))
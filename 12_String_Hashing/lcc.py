import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


MOD = 10**9 + 7
BAS = 200



def get_hash(s):
    cur = 0
    for i in range(len(s)):
        #print(i, s[i])
        cur = (cur * BAS) % MOD
        cur = (cur + ord(s[i])) % MOD
    return cur

def ok(s, n ,hsh):
    #print(n)
    if n == 0:
        return True
    if n == 1:
        for str in list(s):
            if ord(str) == hsh:
                return True
            
    cur = 0
    rem = BAS ** (n-1)

    for i in range(n):
        #print(i, s[i])
        cur = (cur * BAS) % MOD
        cur = (cur + ord(s[i])) % MOD
    
    if cur == hsh: return True
    for i in range(n, len(s)):
        #remove
        #print(s[i-n], s[i])
        cur = (cur - ord(s[i - n]) * (rem)) % MOD
        cur = (cur * BAS + ord(s[i])) % MOD
        
        #print(i, i-n, s[i-n: i], s[i-n], s[i], cur)
        if cur == hsh: return True

    return False

def check(arr,minI, mid, minL,):
    #print(mid)
    allOk = True
    for sub in range((minL - mid)+1):
        allOk = True
        str = arr[minI][sub:sub+mid]
        #print(str)
        hsh = get_hash(str)
        #print(hsh)
        for i in range(len(arr)):
            if i != minI:
                if not ok(arr[i], mid, hsh):
                    allOk = False
                    break
        if allOk: return True
    return False
        
    
#Binary search for higher bound
def high_bound(arr, minI, minL):
    l, r,  = 0, minL+1
    ans = -1
    while l < r:
        mid = (l + r) // 2
        #print(l, r, mid)
        if check(arr, minI, mid, minL):
            ans = mid
            l = mid+1
        else:
            r = mid
    return ans
       
def solve():
    l = ni()
    arr = []
    maxL = 0
    minL = 10000000000
    minI = 0
    for _ in range(l):
        ss = INP()
        maxL = max(maxL, len(ss))
        if len(ss) < minL:
            minL = len(ss)
            minI = _
        arr.append(ss)
    #high bound 
    #print(minI, minL)
    print(high_bound(arr, minI, minL))


solve()
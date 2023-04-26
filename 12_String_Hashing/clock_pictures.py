import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

MOD = 10**16 + 61

def solve(n,a, b):
    if n == 1:
        return True
    #at position i (0 < a_i < 360 000)
    newA = []
    newB = []
    a.sort()
    b.sort()
    #print(a, b)
    for i in range(n-1):
        newA.append(a[i+1] - a[i])
        newB.append(b[i+1] - b[i])
    newA.append(a[0] + 360000 - a[-1])
    newB.append(b[0] + 360000 - b[-1])
    newA += newA
    print(newA)
    print(newB)

    p = 10**16 + 61	 # number that will be multiplied by
    
    
    curP = 1
    hashofB = 0
    
    # check if B exists in a

    print()
    for i in range(len(newB)):
        print(i, newB[i], curP, newB[i] * curP)
        hashofB = (hashofB + newB[i] * curP) % MOD
        curP = (curP * p) % MOD
        
    print(hashofB)
        
    hash1 = 0
    curP = 1
    print()
    for i in range(len(newB)):
        print(i, newA[i], curP, newA[i] * curP)
        hash1 = (hash1 + newA[i] * curP) % MOD
        curP = (curP * p) % MOD
        
    print(hash1)
    
    if hash1 == hashofB:
        return True
    
    print()
    #now for the rolling part
    big = (p ** (len(newB) - 1))  % MOD
    print(big)
    trail = 0
    print()
    print(90000 * p)
    print(MOD)
    for i in range(len(newA)//2, len(newA)):
        print(i, trail, newA[trail], (hash1 - newA[trail]), (hash1 - newA[trail]) / p)
    
        hash1 = ((hash1 - newA[trail]) / p + (newA[i] * big)) % MOD
        trail += 1
        if hash1 == hashofB:
            return True
    return False

l = ni()
a, b = nl(), nl()
if solve(l, a, b):
    print("possible")
else:
    print("impossible")
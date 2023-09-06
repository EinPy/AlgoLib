import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

M = 3600
#Bfs to find distannce to all nodes in graph 
def bfs(adj):
    q = [0]
    dists = [-1 for _ in range(M+1)]
    dists[0] = 0
    while q:
        q2 = []
        for u in q:
            for delta in adj:
                newT = u + delta
                if newT < 0:
                    newT = 0
                if newT > M:
                    newT = M
                if dists[newT] == -1:
                    dists[newT] = dists[u] + 1
                    q2.append(newT)
        q = q2
    return dists

def solve(b, targ):
    d = bfs(b)
    for i in range(targ, M+1):
        if d[i] != -1:
            print(d[i], i - targ)
            return 


t = ni()
for case in range(t):
    nb, targ = nl()
    buttons = nl()
    solve(buttons, targ)
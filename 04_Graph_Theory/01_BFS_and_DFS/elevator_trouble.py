import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]






f, s, g, u, d = nl()


#Bfs to find distannce to all nodes in graph 
def bfs():
    q = [s]
    dists = [-1 for _ in range(f+1)]
    dists[s] = 0
    while q:
        q2 = []
        for v in q:
            if dists[v] > 1000001:
                break
            for nf in (v + u, v - d):
                if 1 <= nf <= f and dists[nf] == -1:
                    dists[nf] = dists[v] + 1
                    q2.append(nf)
        q = q2
    if dists[g] != -1:
        print(dists[g])
    else:
        print("use the stairs")
bfs()

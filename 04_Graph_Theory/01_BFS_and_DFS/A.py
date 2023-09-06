import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


#Bfs to find distannce to all nodes in graph 
def bfs(adj, vis, s):
    q = [s]
    while q:
        q2 = []
        for u in q:
            for n in adj[u]:
                if vis[n] == False:
                    vis[n] = True
                    q2.append(n)
        q = q2
    return vis


def solve(adj):
    vis = [False for _ in range(len(adj))]
    c = -1
    for node in range(len(vis)):
        if not vis[node]:
            vis[node] = True
            vis = bfs(adj, vis, node)
            #print(vis)
            c += 1
    print(c)
    


t = ni()
for case in range(t):
    m = ni()
    adj = [[] for _ in range(m)]
    r = ni()
    for line in range(r):
        a, b = nl()
        adj[a].append(b)
        adj[b].append(a)
    solve(adj)

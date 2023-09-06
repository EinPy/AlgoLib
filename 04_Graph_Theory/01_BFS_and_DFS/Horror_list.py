import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def bfs(adj, h_list):
    q = h_list
    scores = [-1 for _ in range(len(adj))]
    horr = [False for _ in range(len(adj))]
    for idx in h_list:
        scores[idx] = 0
        horr[idx] = True
    while q:
        v = q.pop(0)
        for u in adj[v]:
            if not horr[u] and scores[u] == -1:
                scores[u] = scores[v] + 1
                print("add: " , u)
    return scores

def solve(adj, h_list):
    scores = bfs(adj, h_list)
    best = max(scores)
    print(scores)
    low = min(scores)
    if low == -1:
        for i, v in enumerate(scores):
            if v == low:
                return i 
    for i, v in enumerate(scores):
        if v == best:
            return i
    

num, h, l = nl()
h_list = nl()
adj = [[] for _ in range(num)]
for r in range(l):
    a, b = nl()
    adj[a].append(b)
    adj[b].append(a)
    
    
print(solve(adj, h_list))
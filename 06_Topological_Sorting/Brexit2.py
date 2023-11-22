#https://open.kattis.com/contests/nqjuqd/problems/brexit
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


from collections import deque

def kahn(adj, l, x):
    #find inDegree
    in_deg = [0] * len(adj)
    for u in adj:
        for v in u:
            in_deg[v] += 1
            
    orgpartner = [len(u) for u in adj]
    curPartner = orgpartner[:]
    q = deque([l])
    top_order = []
    inUnion = [True for _ in range(len(adj))]
    inUnion[l] = False
    
    while q:
        #layer by layer
        u = q.popleft()
        if u == x:
            print("leave")
            return
        top_order.append(u)
        
        for v in adj[u]:
            if inUnion[v]:
                curPartner[v] -= 1 #remove incoming node
                if curPartner[v] <= orgpartner[v] // 2:
                    q.append(v)
                    inUnion[v] = False
                    
    if x in top_order: #there is a cycle
        print("leave")
    else:
        print("stay")




c, p, x, l = nl()
x  -= 1
l -= 1

adj = [[] for _ in range(c)]
for _ in range(p):
    a, b = nl()
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

kahn(adj, l, x)
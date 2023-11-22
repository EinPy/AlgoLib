import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def bfs(adj, s):
    q = [s]
    vis = {}
    newG = defaultdict(list)
    while q:
        q2 = []
        for u in q:
            for v in adj[u]:
                if v not in vis:
                    vis[v] = True
                    q2.append(v)
                    newG[u].append(v)
        q = q2
    #print(newG)
    return newG

def kahn(adj, s):
    #find inDegree
    in_deg = defaultdict(int)
    for u in adj.keys():
        if u not in in_deg:
            in_deg[u] = 0
        for v in adj[u]:
            in_deg[v] += 1
    #choose nodes with indegree 0
    #replace q with a priority q to extract the lexographically
    #minial topsort by breaking ties lexographically
    q = deque([s])
    top_order =  []
    #can need visited array if bi-directional edges
    
    while q:
        #layer by layer
        u = q.popleft()
        top_order.append(u)
        
        for v in adj[u]:
            in_deg[v] -= 1 #remove incoming node
            if in_deg[v] == 0:
                q.append(v)
    print("\n".join(top_order))

def solve(adj, s):
    newG = bfs(adj, s)
    #print(adj)
    #print(newG)
    kahn(newG, s)

n = ni()
adj = defaultdict(list) #can do a wrapper but not neccecary if no tle?

for _ in range(n):
    f, dep = INP().split(":")
    #print(f, dep)
    if f not in adj:
        adj[f] = []
    for d in dep.split(" "):
        if d != "":
            adj[d].append(f)
        
s = INP()
solve(adj, s)
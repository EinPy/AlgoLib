import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


def kahn(adj, s):
    #find inDegree
    in_deg = defaultdict(int)
    for u in adj.keys():
        if u not in in_deg:
            in_deg[u] = 0
        for v in adj[u]:
            in_deg[v] += 1
    #choose nodes with indegree 0
    #remove all nodes that can be removed without looking at starting node
    #print(in_deg)
    q = deque([u for u in in_deg.keys() if in_deg[u] == 0 and u != s])
    #remove all nodes that can be topsorted away without dermoving start node
    
    while q:
        #layer by layer
        u = q.popleft()
        
        for v in adj[u]:
            in_deg[v] -= 1 #remove incoming node
            if in_deg[v] == 0 and v != s:
                q.append(v)

    q = deque([s])
    top_ord = []
    
    while q:
        #layer by layer
        u = q.popleft()
        top_ord.append(u)
        for v in adj[u]:
            in_deg[v] -= 1 #remove incoming node
            if in_deg[v] == 0:
                q.append(v)
    print("\n".join(top_ord))

n = ni()
adj = defaultdict(list) #can do a wrapper but not neccecary if no tle?

for _ in range(n):
    f, dep = INP().split(":")
    if f not in adj:
        adj[f] = []
    for d in dep.split(" "):
        if d not in adj:
            adj[d] = []
        if d != '':
            adj[d].append(f)
        
s = INP()
#print(adj)
kahn(adj, s)
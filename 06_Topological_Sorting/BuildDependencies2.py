import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



from collections import deque
#first find all involved dependencies, then do a topsort of them

def kahn(adj, s):
    #find inDegree
    in_deg = defaultdict(int)
    for u in adj:
        for v in u:
            in_deg[v] += 1
    #choose nodes with indegree 0
    #replace q with a priority q to extract the lexographically
    #minial topsort by breaking ties lexographically
    q = deque([s])
    top_order =  []
    vis = defaultdict(bool)
    vis[s] = True
    #can need visited array if bi-directional edges
    newG = defaultdict(list)
    
    while q:
        #layer by layer
        u = q.popleft()
        top_order.append(u)
        
        for v in adj[u]:
            in_deg[v] -= 1 #remove incoming node
            if v not in vis:
                #newG[v].append(u)
                newG[u].append(v)
                q.append(v)
                vis[v] = True
                
    #print(newG)
    in_deg = defaultdict(int)
    for u in newG.keys():
        for v in newG[u]:
            in_deg[v] += 1
    
    #print(in_deg)
    #choose nodes with indegree 0
    #replace q with a priority q to extract the lexographically
    #minial topsort by breaking ties lexographically
    q = deque([s])
    top_order =  []
    vis = defaultdict(bool)

    
    while q:
        #layer by layer
        u = q.popleft()
        top_order.append(u)
        
        for v in adj[u]:
            in_deg[v] -= 1 #remove incoming node
            if in_deg[v] == 0:
                q.append(v)
        
    print("\n".join(top_order))


n = ni()
adj = defaultdict(list) #can do a wrapper but not neccecary if no tle?

for _ in range(n):
    f, dep = INP().split(":")
    for d in dep.split(" "):
        adj[d].append(f)
        
s = INP()
kahn(adj, s)
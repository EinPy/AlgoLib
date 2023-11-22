from collections import deque

def kahn(adj):
    #find inDegree
    in_deg = [0] * len(adj)
    for u in adj:
        for v in u:
            in_deg[v] += 1
    #choose nodes with indegree 0
    #replace q with a priority q to extract the lexographically
    #minial topsort by breaking ties lexographically
    q = deque([u for u in in_deg if in_deg[u] == 0])
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
    if len(top_order != len(adj)): #there is a cycle
        return [-1]
    return top_order


#djikstra ashortest path in weighted graph. 
from heapq import heappush, heappop
# S: Start node
# G: [[(to_node, weight)]], for instance [[(1,3), (0,3), ...], [...], ...]
#return shortes dists to all
INF = 10**9
def djikstra (S, G):
    dists = [INF] * len(G)
    heap = []
    heappush(heap, (0,S))
    dists[S] = 0
    
    while heap:
        d, u = heappop(heap)
        for v, c in G[u]:
            alt = d + c
            if alt < dists[v]:
                dists[v] = alt
                heappush(heap, (alt, v))
                
    return dists

#return shortest path
def djikstra(S, F, G):
    dists = [INF] * len(G)
    parent = [None] * len(G)
    heap = []
    heappush(heap, (0,S))
    dists[S] = 0
    
    while heap:
        d, u = heappop(heap)
        if u == F: return d
        if d > dists[u]: continue
        for v, c in G[u]:
            alt = d + c
            if alt < dists[v]:
                dists[v] = alt
                parent[v] = u
                heappush(heap, (alt, v))
                
    if dists[F] == INF: return None
    path = []
    curr = F
    while curr != None:
        path.append(curr)
        curr = parent[curr]
                
    return path[::-1]
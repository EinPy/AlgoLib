import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


#Code starts here


def topSort(graph, L, X):
    if L == X:
        return "leave"
    n = len(graph)
    inDeg = [0 for _ in range(n)]
    for i in range(n):
        for p in graph[i]:
            inDeg[p] += 1
            
    orgInDeg = inDeg[:]
        
    queue = deque([L])
    
    inUnion = [True] * len(graph)
    inUnion[L] = False
    
    while queue:
        #get next node from queue
        node = queue.popleft()
        #add it to the order

        #process neighbours and reduce their indegree by one
        for n in graph[node]:
            if inUnion[n]:
                inDeg[n] -= 1
                if inDeg[n] <= orgInDeg[n] / 2:
                    #The city has lost half of its trading partners and 
                    #will leave the union
                    queue.append(n)
                    inUnion[n] = False
                    if n == X:
                        return "leave"

#print(inDeg, orgInDeg)

                
    return "stay"
                

C, P, X, L = nl()
L -= 1
X -= 1
graph = [[] for _ in range(C)]
for e in range(P):
    A, B = nl()
    A -= 1
    B -= 1
    graph[A].append(B)
    graph[B].append(A)
    
#print(C, P, X, L )
#print(graph)
print(topSort(graph, L, X))

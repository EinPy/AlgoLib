import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)
def ni(): return int(input())
def nl(): return [int(_) for _ in input().split()]




def topologicalSort(graph, start):
    n = len(graph)
    inDeg = {}
    for k in graph.keys():
        if k not in inDeg:
            inDeg[k] = 0
        for p in graph[k]:
            if p not in inDeg:
                inDeg[p] = 
            else:
                inDeg[p] += 1
        
    queue = [start]
    
    order = []
    while queue:
        #get next node from queue
        node = queue.pop(0)
        #add it to the order
        order.append(node)
        
        #process neighbours and reduce their indegree by one
        for n in graph[node]:
            inDeg[n] -= 1
            if inDeg[n] == 0:
                #The node now has inDegree 0 and can be added to queue
                queue.append(n)
                
    return order



N = ni()
print(N)
dependencies = {}
for _ in range(N):
    f = input().split(':')
    deps = f[1].split()
    if f[0] not in dependencies:
        dependencies[f[0]] = []
    for d in deps:
        if d not in dependencies:
            dependencies[d] = [d]
        dependencies[d].append(f[0])
    
print(dependencies)
change = input()

topSort(dependencies, change)
#To start code
import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)



n, m = list(map(int,input().split()))
graph = [[] for _ in range(n)]
inDeg = [0 for _ in range(n)]
for edge in range(m):
    prequesite, job = list(map(int,input().split()))
    graph[prequesite-1].append(job-1)
visited = [False] * n
ans = []
#print(graph)


def topologicalSort(graph):
    n = len(graph)
    inDeg = [0 for _ in range(n)]
    for i in range(n):
        for p in graph[i]:
            inDeg[p] += 1
        
    queue = []

    for i in range(n):
        if inDeg[i] == 0:
            queue.append(i)
    
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

ans = topologicalSort(graph)
if len(ans) != len(graph):
    print("IMPOSSIBLE")
else:
    for el in ans:
        print(el+1)
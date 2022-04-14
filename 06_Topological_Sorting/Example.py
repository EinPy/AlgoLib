
#number of verticies
import queue


n = int(input())
graph = [()] #adjecency list
visited = [False] * n
ans = []

#one way to do it with dfs, however,
#this assumes the graph is acyclic. 

def dfs(v):
    visited[v] = True
    for neighbour in graph[v]:
        if not visited[neighbour]:
            dfs(neighbour)
    ans.append(v)
    
def topSort():
    for i in range(n):
        if not visited[i]:
            dfs(i)
    return ans[::-1]

#Better way, here you can check if the remaining
#in degree of all nodes is 0, and if not, the graph contains
#a cycle. However, the nodes who's indegree are nonzero are not 
#neccecarily a cycle. 

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
                
                
print(topologicalSort([[1],[2],[1]]))
    
    
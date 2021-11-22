## BFS ##

A fundemaneteal serach argorithm used to xplore nodes and edges of a graph.
Runs with T.C O(N+V), That is nodes + edges. 
It is often used as a building block in other algorithms and is 
most commonly used to find the shortest path in an unweighted graph.

It explores nodes in layers around it, like ripples in a pool. 
That is, it visits it's all immediate neighbours first, then next level 
neighbours. It uses a queue to keep track of the order. 


Pseudo code overview:
```
imagine global variables:
n = number of nodes in the graph
g = adjecency list representing unweighted graph

# s = start node, e = end node, and 0 <= e, s <neighbours
function bfs(s,e):
	#do a BFS starting at node s
	prev = solve(s)

	#return reconstructed path from s -> e
	return reconstructPath(s, e, prev)
```

More detailedd pseudo code of solve():
```
def solve(s):
q queue data structure wiith enqueue and dequeue
q.enqueue(s)

visitied = [False, ..., False] #size n
visited[s] = True

prev = [null, ..., null] #size n, will help reconstruct path, not always needed
while !q.isEmpty(): #while queue is not empty
	node = q.dequeue() # pulls top node
	neighbours = g.get(node) #reach in adjacency list and find neighbours

	for next in neighbours:
		if !visited[next]:
			q.enqueue(next)
			visited[next] = True
			prev[next] = node
	return prev
```
More detailedd pseudo code of reconstructPath():
```
def reconstructPath(s, e, prev):
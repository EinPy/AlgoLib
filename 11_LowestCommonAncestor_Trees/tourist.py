import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n = ni()
adj = [[] for _ in range(n)]
for line in range(n-1):
    a,b = nl()
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

# -- root a tree in node 0 without recursion --
parent = [0] * n # fill with 0 so the parent of the root becomes itself, otherwise fill with -1
children = [[] for i in range(n)]
depth = [0] * n
dfsStack = [0]
edgeIdx = [0] * n
while dfsStack:
	cur = dfsStack[-1]
	if edgeIdx[cur] == len(adj[cur]):
		dfsStack.pop()
	else:
		child = adj[cur][edgeIdx[cur]]
		if child != parent[cur]:
			dfsStack.append(child)
			children[cur].append(child)
			parent[child] = cur
			depth[child] = depth[cur] + 1
		edgeIdx[cur] += 1 


# -- compute jump table --
jump = [[-1] * n for i in range(20)]
jump[0] = parent # sets all first-level jumps to the parent
for lvl in range(1, len(jump)):
	for i in range(n):
		jump[lvl][i] = jump[lvl-1][jump[lvl-1][i]]


# -- get parent function --
def getParent(node, dist):
	for lvl in range(len(jump)):
		if dist & (1 << lvl):
			node = jump[lvl][node]
	return node


# -- lca function --
def findLCA(a, b):
	if depth[b] > depth[a]:
		a, b = b, a # swap so that a is deeper than b
	a = getParent(a, depth[a] - depth[b]) # move a up to the same depth as b
	if a == b:
		return a
	for i in range(len(jump) - 1, -1, -1):
		if jump[i][a] != jump[i][b]:
			a = jump[i][a]
			b = jump[i][b]
	return parent[a]

#print(parent)
totDist = 0
for x in range(1,n+1):
    mult = x
    while mult <= n:
        if x != mult:
            lca = findLCA(x-1, mult-1)
            d =  depth[x-1] + depth[mult-1] - 2 * depth[lca] 
            totDist +=d + 1
            #print(x, mult, lca, d, depth[x-1], depth[mult-1], depth[lca])
        mult += x
print(totDist)
        
        

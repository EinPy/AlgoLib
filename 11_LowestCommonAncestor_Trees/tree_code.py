# -- root a tree in node 0 with recrusion --
parent = [0] * n # fill with 0 so the parent of the root becomes itself, otherwise fill with -1
children = [[] for i in range(n)]
depth = [0] * n
def rootTree(node):
	for nxt in adj[node]:
		if nxt != parent[node]:
			parent[nxt] = node
			children[node].append(nxt)
			depth[nxt] = depth[node] + 1
			rootTree(nxt)
rootTree(0)


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

# jump[k][i] is 2**k jump for node i 
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
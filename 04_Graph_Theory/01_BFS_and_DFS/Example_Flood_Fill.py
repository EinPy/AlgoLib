#not yet complete
def setupInputOutputSublime():
	import sys
	sys.stdout = open("C:\\Users\\einar\\OneDrive\\Skrivebord\\output.txt", mode = 'w')
	sys.stdin = open("C:\\Users\\einar\\OneDrive\\Skrivebord\\intput.txt", mode = 'r')
setupInputOutputSublime()

#code starts here
from queue import Queue

testGraph = [[1,1,1],[1,1,0],[1,0,1]]
sr, sc, newColor = 1, 1, 2
tst = [0 for _ in range(10)]
print(tst)

def flood_fill_bfs(sr, sc, newColor):
	org_color = testGraph[sr][sc]
	q = []
	start_cord = (sr, sc)
	q.append(start_cord)
	for i in q: print(i)
	visited = [[False for i in range(len(testGraph[0]))] for _ in range(len(testGraph))]
	for i in visited:
		print (i)

	visited[start_cord[0]][start_cord[1]] = True

	while q:
		node = q.pop(0)
		neighbours = get_neighbours(node, testGraph)

		for neighbour in neighbours:
			if not visited[neighbour[0]][neighbour[1]]:
				if testGraph[neighbour[0]][neighbour[1]] == org_color:
					q.append(neighbour)
					visited[neighbour[0]][neighbour[1]] = True

	for row in range((len(testGraph[0]))):
		for col in range(len(testGraph[1])):
			if visited[row][col] == True:
				testGraph[row][col] = newColor

	print(testGraph)

def get_neighbours(node, adj_lst):
	neighbours = []
	for row_shift in range(-1, 2, 2):
		if node[0] + row_shift >= 0 and node[0] + row_shift <= len(adj_lst):
			neighbours.append((node[0] + row_shift,node[1]))
	for col_shift in range(-1,2, 2):
			if node[1] + col_shift >= 0 and node[1] + col_shift <= len(adj_lst[1]):
					neighbours.append((node[0],node[1] + col_shift))
	return neighbours
	



flood_fill_bfs(sr,sc,newColor)



for i in range(-1,2, 2):
	print(i)

print(get_neighbours((0,0),testGraph))


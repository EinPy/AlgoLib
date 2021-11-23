#input setup, not relevant for solution
def setupInputOutputSublime():
	import sys
	sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
	sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
setupInputOutputSublime()

#Solution to: https://leetcode.com/problems/flood-fill/
#code starts here
    def floodFill(image, sr, sc, newColor):
        org_color = image[sr][sc]
        q = []
        start_cord = (sr, sc)
        q.append(start_cord)
    #	for i in q: print(i)
    #	print("\n")
        visited = [[False for i in range(len(image[0]))] for _ in range(len(image))]
    #	for i in visited:
    #		print (i)
    #	print("\n")

        visited[start_cord[0]][start_cord[1]] = True

        while q:
            node = q.pop(0)

            neighbours = []
            for row_shift in range(-1, 2, 2):
                if node[0] + row_shift >= 0 and node[0] + row_shift <= len(image)-1:
                    neighbours.append((node[0] + row_shift,node[1]))
            for col_shift in range(-1,2, 2):
                    if node[1] + col_shift >= 0 and node[1] + col_shift <= len(image[1])-1:
                            neighbours.append((node[0],node[1] + col_shift))

            for neighbour in neighbours:
                if not visited[neighbour[0]][neighbour[1]]:
                    if image[neighbour[0]][neighbour[1]] == org_color:
                        q.append(neighbour)
                        visited[neighbour[0]][neighbour[1]] = True

        for row in range((len(image))):
            for col in range(len(image[1])):
                if visited[row][col] == True:
                    image[row][col] = newColor

        return image


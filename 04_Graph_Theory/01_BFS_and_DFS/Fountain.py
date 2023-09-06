import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



#bfs when graph is grid
#can return visited if you want to find how many connected graphs there are
def bfsGrid(grid):
    R = len(grid)
    C = len(grid[0])
    q = deque([])
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "V":
                q.append((r,c))
    while q:
        r,c = q.popleft()
        nr, nc = r + 1, c
        if 0 <= nr < R and 0 <= nc < C:
            if grid[nr][nc] == ".":
                grid[nr][nc] = "V"
                q.append((nr, nc))
            if grid[nr][nc] == "#":
                if nc +1 < C and grid[r][nc+1] == ".":
                    grid[r][nc+1] = "V"
                    q.append((r,nc+1))
                if nc - 1 >= 0 and grid[r][nc-1] == ".":
                    grid[r][nc - 1] = "V"
                    q.append((r, nc - 1))
    for row in grid:
        print("".join(row))

n, m = nl()
g = []
for i in range(n):
    g.append(list(INP()))    
    
#print(g)
bfsGrid(g)
    
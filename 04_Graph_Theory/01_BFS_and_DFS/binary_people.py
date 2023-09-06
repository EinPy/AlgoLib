import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    pass


x, xx = nl()
g = []
for _ in range(x):
    g.append(list(INP()))
    
idx = 1
vis = [[-1 for _ in range(xx)] for _ in range(x)]


#bfs when graph is grid
#can return visited if you want to find how many connected graphs there are
def bfsGrid(r, c, hash):
    T = g[r][c]
    R = len(g)
    C = len(g[0])
    q = deque([(r,c)])
    vis[r][c] = hash

    while q:
        r,c = q.popleft()
        for nr, nc in [(r-1,c), (r+1, c), (r, c+1), (r,c-1)]:
            if 0 <= nr < R and 0 <= nc < C:
                tup = nr, nc
                if vis[nr][nc] == -1 and g[nr][nc] == T: #add other conditions here
                    vis[nr][nc] = hash
                    q.append(tup)
    return 

for r in range(x):
    for c in range(xx):
        if vis[r][c] == -1:
            bfsGrid(r, c, idx)
            idx += 1
            
            
q = ni()
# for r in vis:
#     print(r)
for _ in range(q):
    r1,c1, r2, c2 = nl()
    if vis[r1-1][c1-1] != vis[r2-1][c2-1]:
        print("neither")
    else:
        if g[r1-1][c1-1] == "0":
            print("binary")
        else:
            print("decimal")
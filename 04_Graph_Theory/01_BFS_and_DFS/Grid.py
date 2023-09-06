
import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)


def solve(graph,R,C):
    q = [(0,0)]
    dists = [[0 for _ in range(C)] for _ in range(R)]
    while q:
        q2 = []
        for r, c in q:
            k = graph[r][c]
            for nr, nc in [(r-k,c), (r+k, c), (r, c+k), (r,c-k)]:
                if 0 <= nr < R and 0 <= nc < C:
                    tup = nr, nc
                    if not dists[nr][nc]:
                        dists[nr][nc] = dists[r][c] + 1
                        if dists[-1][-1]:
                            return dists[-1][-1]
                        q2.append(tup)
        q = q2
    return -1
            
            
        

R, C  = list(map(int,input().split()))
graph = []
for i in range(R):
    line = input()
    row = []
    for i in line:
        row.append(int(i))
    graph.append(row)
print(solve(graph,R,C))

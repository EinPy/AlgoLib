#To start code
import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)



C, P, X, L = list(map(int,input().split()))
graph = [[] for _ in range(C)]
for e in range(P):
    A, B = list(map(input().split()))
    graph[A].append(B)
    graph[B].append(A)
    
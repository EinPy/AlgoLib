#solution to https://open.kattis.com/problems/fulltank

"""
After going through the receipts from your car trip through Europe this summer, 
you realised that the gas prices varied between the cities you visited.
Maybe you could have saved some money if you were a bit more clever about where you filled your fuel?

To help other tourists (and save money yourself next time), 
you want to write a program for finding the cheapest way to travel between cities, 
filling your tank on the way. We assume that all cars use one unit of fuel per unit of distance, 
and start with an empty gas tank.

Input
The first line of input gives 1≤n≤1000 and 0≤m≤10000, 
the number of cities and roads. 
Then follows a line with n integers 1≤pi≤100, 
where pi is the fuel price in the ith city. Then follow m lines with three integers
 0≤u,v<n and 1≤d≤100, telling that there is a road between u and v with length d. 
 Then comes a line with the number 1≤q≤100, giving the number of queries, and q lines with three integers
  1≤c≤100, s and e, where c is the fuel capacity of the vehicle, s is the starting city, and e is the goal.

Output
For each query, output the price of the cheapest trip from
 s to e using a car with the given capacity, or “impossible” if there is no way of getting from s to e with the given car.
"""

"""
Lessons learned:
No matter how large the graph is, it is always bet to keep track of dists
with an array. 

The dists array can be of multiple dimensions if something is tracked over multiple states

To duplicate a graph, you do not need to actually make a new graph with more nodes.
When you are one a node, you simply add the same, or a diffrent already existing node
to the que again, with some change in a parameter when some condition is met.

"""







import sys
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code
#solution to https://open.kattis.com/problems/fulltank


#standard template
def solve(n,m,p,graph,c,s,e):
#    print(graph)
    print(djikstra(s,e,graph,c, n, p))


INF = 10**9
#djikstra ashortest path in weighted graph. 
from heapq import heappush, heappop
# G: [[(to_node, weight)]], for instance [[(1,3), (0,3), ...], [...], ...]
#input is start, finish, graph, fuelTankSize, amount of node, price list
def djikstra(S, F, G, c, n, p):
    dists = [[INF for _ in range(n)] for _ in range(c+1)]
#    print(dists)
    heap = []
    #tot cost, node, curTank
    heappush(heap, (0,S,0))
    dists[0][S] = 0
    
    while heap:
        cost, node, tank = heappop(heap)
        if node == F: return cost
        for vertex, dist in G[node]:
            fuel = tank - dist
            if fuel >= 0 and fuel <= c:
                if cost < dists[fuel][vertex]:
                    dists[fuel][vertex] = cost
                    heappush(heap,(cost, vertex, fuel))

        if tank < c:
            fuel = tank + 1
            cost += p[node]
            if cost < dists[fuel][node]:
                dists[fuel][node] = cost
                heappush(heap,(cost, node, fuel))

    if dists[0][F] == INF: return "impossible"
    return dists[0][F]






def run():
    n, m = list(map(int,input().split()))
    p = list(map(int,input().split()))
    graph = [[] for _ in range(n)]
    for edge in range(m):
        u, v, d = list(map(int,input().split()))
        graph[u].append((v, d))
        graph[v].append((u, d))
        
        
    q = int(input())
    for query in range(q):
        c, s, e = list(map(int,input().split()))
        solve(n,m,p,graph,c,s,e)


run()
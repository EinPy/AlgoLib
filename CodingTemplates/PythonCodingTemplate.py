from math import sqrt

def gcd(a, b):
	if a == 0:
		return b
	return gcd(b%a, a)

def lcm(a, b):
	product = a*b
	#highest common factor == greatest common divisor
	hcf = gcd(a, b)
	return product // hcf

def allDivisors(n):
	#O(sqrt(n))
	div2 = set()
	for i in range(1, int(sqrt(n))+1): #range [1, root(n)]
		if n%i == 0:
			div2.add(i)
			div2.add(n//i)
	return div2

def primeTest(n):
	#T.C = O(root(n))
	if n == 0 or n == 1: #O(1)
		return False
	if n == 2 or n == 3: #O(1)
		return True
	if n%2 == 0 or n%3 == 0: #O(1)
		return False
	for i in range(5,int(sqrt(n))+1): # [1, root (n)]
		if n%i == 0 or n%(i+2) == 0:
			return False
	return True

def generate_primes(n):
	primes = [True]*(n+1)
	primes[0], primes[1] = False, False
	for p in range(2, int(sqrt(n)) + 1):
		if primes[p]:
			for i in range(p*p, n+1, p):
				primes[i] = False

	out = []
	for i, n in enumerate(primes):
			if n:
				out.append(i)
	return out

def crossZ(p, q):
	return p[0]*q[1] - q[0]*p[1]

def vec(p, q):
	return q[0] - p[0], q[1] - p[1]


# Converts two points to a line (a, b, c), 
# ax + by + c = 0
# if p == q, a = b = c = 0
def pts2line(p, q):
	a = -q[1] + p[1]
	b = q[0] - p[0]
	c = p[0]*q[1] - p[1]*q[0]
	return (a, b, c)


def normalize(a,b,c):
	if a == 0:
		return 0, 1, Fraction(c, b)
	if a < 0:
		a, b, c = -a, -b, -c
	factor = gcd(a, abs(b))
	a, b, c = a//factor, b//factor, Fraction(c, factor)
	return a, b, c


def is_multiple(x,y):
    if x!=0 and (y%x)==0:
    	return True
    elif x!= 0 and (x%y) == 0:
    	return True

def convexHull(points): #input in typles with coordinates (x,y)
	points.sort() #sort by x
	def getHull(points):
		UPP = [] # upper part of Hull
		#adding the two leftmost points
		UPP.append(points[0])
		UPP.append(points[1])
		for p in points[2:]:
			while len(UPP) > 1: 
				v1 = vec(UPP[-1], UPP[-2])
				v2 = vec(UPP[-1], p)
				if crossZ(v1, v2) > 0:
					break 
				UPP.pop()
			UPP.append(p)
		return UPP
	UPP = getHull(points)
	LOW = getHull(points[::-1])

	return UPP[1:] + LOW[1:]


#Bfs to find distannce to all nodes in graph 
def bfs(Graph, S):
    q = [S]
    dists = {S:0}
    while q:
        q2 = []
        for u in q:
            for n in Graph[u]:
                if n not in dists:
                    dists[v] = dists[u] + 1
                    q2.append(v)
        q = q2
    return dists

#bfs when graph is grid
#can return visited if you want to find how many connected graphs there are
def bfsGrid(grid, r, c):
    R = len(grid)
    C = len(grid[0])
    q = [(r,c)]
    dists = [[-1 for _ in range(C)] for _ in range(R)]
    while q:
        q2 = []
        for r, c in q:
            for nr, nc in [(r-1,c), (r+1, c), (r, c+1), (r,c-1)]:
                if 0 <= nr <= R and 0 <= nc < C:
                    tup = nr, nc
                    if dists[nr][nc] == -1: #add other conditions here
                        dits[tup] = dists[r,c] + 1
                        q2.append(tup)
        q = q2
    return dists


#djikstra ashortest path in weighted graph. 
from heapq import heappush, heappop
# S: Start node
# G: [[(to_node, weight)]], for instance [[(1,3), (0,3), ...], [...], ...]
#return shortes dists to all
INF = 10**9
def djikstra (S, G):
    dists = [INF] * len(G)
    heap = []
    heappush(heap, (0,S))
    dists[S] = 0
    
    while heap:
        d, u = heappop(heap)
        for v, c in G[u]:
            alt = d + c
            if alt < dists[v]:
                dists[v] = alt
                heappush(heap, (alt, v))
                
    return dists

#return shortest path
def djikstra(S, F, G):
    dists = [INF] * len(G)
    parent = [None] * len(G)
    heap = []
    heappush(heap, (0,S))
    dists[S] = 0
    
    while heap:
        d, u = heappop(heap)
        if u == F: return d
        if d > dists[u]: continue
        for v, c in G[u]:
            alt = d + c
            if alt < dists[v]:
                dists[v] = alt
                parent[v] = u
                heappush(heap, (alt, v))
                
    if dists[F] == INF: return None
    path = []
    curr = F
    while curr != None:
        path.append(curr)
        curr = parent[curr]
                
    return path[::-1]


#To start code
import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)
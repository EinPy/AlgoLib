from ast import If
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


n, r, k = nl()
initialG = [[0 for _ in range(n)] for _ in range(n)]
lamps = []
for l in range(1,k+1):
    i,j = nl()
    initialG[i-1][j-1] = l
    lamps.append((i,j))

#index 2i is true, 2i + 1 is false

adj, adjT = [[] for _ in range(2*k)], [[] for _ in range(2*k)]
used = [False for _ in range(2*k)]
#print(used)
order, comp = [], [-1 for _ in range(2*k)]
assignment = []
#for row in initialG:
    #print(row)

#for a node k index tk is true and 2k + 1 is false
#na and nb are booleans signaling whether
#a and b are to be negated, if they are negated
#uses xor operator to add 1. 
#add edge between (A OR B)
def addEdge(a, na, b, nb):
    #print(a,b)
    #2a will always be even, XOR (^) adds one if it is supposed to be False
    a = 2* a ^ na
    b = 2* b ^ nb
    #the negation is simply the opposite
    neg_a = a ^1 
    neg_b = b^1
    #not a -> b
    #not b -> a
    adj[neg_a].append(b)
    adj[neg_b].append(a)
    #for the transpose graph
    adjT[b].append(neg_a)
    adjT[a].append(neg_b)

                        
#print("Second method:")
for i in range(k-1):
    for j in range(i+1,k):
        a,b = lamps[i]
        c,d = lamps[j]
        #same row
        if a == c:
            #if both have to be vertical
            #if abs(b-d) <= r:
                #addEdge(i,False, i, False)
                #ddEdge(j, False, j, False)
                #print("force True", i, j)
            if abs(b-d) <= 2*r:
                addEdge(i, True, j, True)
                #print(i, j)
        #same column
        if b == d:
            #if both have to be horizontal
            #if abs(a-c) <= r:
                #addEdge(i, True, i, True)
                #addEdge(j, True, j, True)
                #print("force False", i, j)
            if abs(a-c) <= 2*r:
                addEdge(i, False, j, False)
                #print(i, j)
        
#print(adj)
#print(adjT)
                        
def dfs1(v):
    used[v] = True
    for u in adj[v]:
        if not used[u]:
            dfs1(u)    
    order.append(v)

def dfs2(v, cl):
    
    comp[v] = cl
    #print(comp)
    for u in adjT[v]:
        if comp[u] == -1:
            dfs2(u,cl)

def solve_2SAT():
    #first dfs
    for i in range(2 * k):
        if not used[i]:
            dfs1(i)
    
    #print(order)
    #print(comp)
    j = 0 #to keep track of which strongly connected component
    for i in range(2*k):
        #reversing the order from the dfs1 to 
        #visit the graph in topological order
        #print(order)
        v = order[2*k - i - 1]
        if comp[v] == -1:
            j += 1
            #print(j)
            dfs2(v, j)
    
    assignment = [False for _ in range(k)]
    for i in range(0,2*k, 2):
        if comp[i] == comp[i+1]:
            return 0
        assignment[i//2] = comp[i] > comp[i+1]
        
    return 1

print(solve_2SAT())
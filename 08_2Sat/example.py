import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


n = ni()
adj, adjT = [[] for _ in range(2*n)], [[] for _ in range(2*n)]
used = [False for _ in range(2*n)]
order, comp = [], []
assignment = []



#for a node k index tk is true and 2k + 1 is false
#na and nb are booleans signaling whether
#a and b are to be negated, if they are negated
#uses xor operator to add 1. 
#add edge between (A OR B)
def addEdge(a, na, b, nb):
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
        
    


def dfs1(v):
    used[v] = True
    for u in adj[v]:
        if not used[u]:
            dfs1(u)
    order.append(v)

def dfs2(v, cl):
    comp[v] = cl
    for u in adjT(v):
        if comp[u] == -1:
            dfs2(u,cl)
            
            
def solve_2SAT():
    #first dfs
    for i in range(2 * n):
        if not used[i]:
            dfs1(i)

    comp = [-1 for _ in range(2*n)]
    j = 0 #to keep track of which strongly connected component
    for i in range(2*n):
        #reversing the order from the dfs1 to 
        #visit the graph in topological order
        v = order[2*n - i - 1]
        if comp[v] == -1:
            j += 1
            dfs2(v, j)
    
    assignment = [False for _ in range(n)]
    for i in range(2*n, 2):
        if comp[i] == comp[i+1]:
            return False
        assignment[i/2] = comp[i] > comp[i+1]
        
    return True


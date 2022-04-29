used = [False] * 1000 #some number
adj = [] #adjecency graph
adjRev = [] #reversed reversed adjecency list
order = []
component = []

def dfs1(v):
    used[v] = True
    for u in adj:
        if not used[u]:
            dfs1(u)
            
    order.append(v)
    
def dfs2(v):
    used[v] = True
    component.append(v)
    for u in adjRev:
        if not used[u]:
            dfs2(u)
    
    
def main():
    
    #build graph
    #set all used = False
    
    for i in range(len(adj)):
        if not used[i]:
            dfs1(i)
            
    #set all used = False
    #reverse order
    order = order[::-1]
    
    for v in order:
        if not used[v]:
            dfs2(v)
            
            #process next component
            component = []
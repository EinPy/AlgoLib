'''
You are a traveler on a 2d grid, you begin in the top left
corner and travel to the bottom right. You can only move down or right.
How many different paths can you take on an m * n grid. 
'''

#this is a complete search, that generates all
#possible paths from start to end
#T.C O(2^(r+c))
#S.C S(r+c)
def gridTravler(r,c):
    gridTravler.cnt += 1
    if r == 1 or c == 1:
        return 1
    if r == 0 or c == 0:
        return 0
    return gridTravler(r-1,c) + gridTravler(r, c -1)

gridTravler.cnt = 0


#with memoizatoin with a 2d array
#realize that there is hte same amount of ways to travel 
#through a [r, c] grid as a [c, r] grid, so we can actually 
#optimize this even further to almost cut the cases in half!
#T.C O(r*c) S.C S(r+c) (in dict, otherwise we create entire 
# array to get better lookup time)
def gridTrav(r, c, mem):
    gridTrav.cnt += 1
    if mem[r][c] != -1:
        return mem[r][c]
    #checking for a "flipped" rectangle
    if c < len(mem) and r < len(mem[0]) and mem[c][r] != -1:
        return mem[c][r]
    if r == 1 or c == 1:
        return 1
    if r == 0 or c == 0:
        return 0
    mem[r][c] = gridTrav(r-1,c,mem) + gridTrav(r, c -1,mem)
    return mem[r][c]
gridTrav.cnt = 0


#for debug
def prtGrd(grd):
    for row in grd:
        print(row)


#T.C O(r*c) S.C = O(r*c)
def gridTab(row, col):
    grid = [[0 for _ in range(col)] for _ in range(row)]

    for n in range(col):
        grid[-1][n] = 1

    for i in range(row):
        grid[i][-1] = 1

    for r in range(row-2,-1, -1):
        for c in range(col-2,-1,-1):
            grid[r][c] = grid[r+1][c] + grid[r][c+1]
    
    return grid[0][0]

gridTab.cnt = 0
  
r = 3
c = 7
mem = [[-1 for _ in range(c+1)] for _ in range(r+1)]
print(gridTravler(r,c), gridTravler.cnt)
print(gridTrav(r,c,mem), gridTrav.cnt)
print(gridTab(r,c),gridTab.cnt)

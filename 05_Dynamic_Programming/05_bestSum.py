"""
Write a function that takes a target and an array of numbers. 
Return the shortes combination of numbers that adds up to the
target sum.

If there are multiple combinatinos with the same length you 
may return the shortest one
"""

#T.C brute force solution
#m is target sum and n is length of nums 
#tree is at max m deep, and for each level n children(branching factor)
#at least O(n^m), because that is the amount of recursive calls,
#however, for each recursive call you have to copy an array that is at most m long so
#T.C = O(m*n^m)
#space is an m deep tree + and at most m large array
# space is O(m^2)
def bestSum(nums, targ):
    bestSum.c += 1
    if targ == 0:
        return []
    if targ < 0:
        return False
    
    shortest = False
    
    for n in nums:
        diff = targ - n
        result = bestSum(nums, diff)
        if result != False:
            combination = result + [n]
            if not shortest:
                shortest = combination
            if shortest and len(combination) < len(shortest):
                shortest = combination
        
    return shortest

bestSum.c = 0



#T.C m is target sum and n is length of nums 
#T.C = O(m*m*n), have to branch for every m, and also copy array
#Space complexity with memo array, every pos in mem is at worst 
#m long, so mem by iself is m^2, and then + return array
# O(2m^2) = O(m^2)

def bestSumMem(nums, targ, mem):
    bestSumMem.c += 1
    if targ < 0:
        return False
    if mem[targ] != -1:
        return mem[targ]
    if targ == 0:
        return []
    
    
    shortest = False
    
    for n in nums:
        diff = targ - n
        result = bestSumMem(nums, diff,mem)
        if result != False:
            combination = result + [n]
            if not shortest:
                shortest = combination
            if shortest and len(combination) < len(shortest):
                shortest = combination
                
    mem[targ] = shortest    
    return shortest
bestSumMem.c = 0


a = [1,1,1,1]
t = 10
mem = [-1 for _ in range(t+1)]
n = len(a)
print(bestSum(a,t), bestSum.c, t*n**t)
print(bestSumMem(a,t,mem), bestSumMem.c)
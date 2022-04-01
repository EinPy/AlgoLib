"""
Write a function that takes in a target sum and 
an aarray of numbers as arguments. The function should return
an array containign any combination of elements that add up to exactly
the targetSum

Return null if no combination exists

If multiple, any return is accepted
"""
import sys
sys.setrecursionlimit(10**5)

#T.C tgs = n, len(nums) = m
#n*m recursive calls, for each call copy an array which is linear time
#--> T.C O(n*m^2)
#m recursive memory calls, memo oject will at worst be n*m
#S.C O(n*m)
def howSum(tgs, nums,mem):
    if tgs < 0:
        return None
    if mem[tgs] != -1:
        return mem[tgs]
    if tgs == 0:
        return []
    
    for n in nums:
        diff = tgs - n 
        result = howSum(diff, nums,mem)
        if result != None:
            mem[diff]= result + [n]
            return mem[diff]

    mem[tgs] = None
    return None


a = [7,14,5]
t = 3000
mem = [-1 for _ in range(t+2)]
print(howSum(t,a,mem))

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


def howSumTab(nums, target):
    dp = [0 for _ in range(target+1)]
    dp[0] = []
    
    for i in range(target):
        if dp[i] != 0:
            for n in nums:
                if i + n <= target:
                    if dp[i+n] == 0:
                        dp[i+n] = dp[i] + [n]

    sum = 0
    for el in dp[target]: sum += el 
    return dp[target], sum

a = [7,14,5]
t = 50
mem = [-1 for _ in range(t+2)]
print(howSum(t,a,mem))
print(howSumTab(a,t),)
"""
write a function that takes in a targetSum and 
and array of number as arguments. Return a bool indicating
if it's possible to generate targetSum using numbers from the array

An element can be used as many times as need
All elements are positive
"""

#initial complete search, bottom up
#if n is array length and m is target sum
#T.C O(n^m))
def canSum(nums, target, sum = 0):
    if sum == target:
        return True
    if sum > target:
        return False

    for num in nums:
        if canSum(nums,target,sum+num):
            return True
    return False

#same but reversed, top down
#reduce to subproblem
#if n is array length and m is target sum
#T.C O(n^m))
#S.C O(m)
def canSumRev(nums, target):
    canSumRev.cnt += 1
    if target == 0:
        return True
    if target < 0:
        return False

    for num in nums:
        if canSumRev(nums,target-num):
            return True
    return False
canSumRev.cnt = 0

#reversed with emmoization 
#if n is array length and m is target sum
#T.C O(n*m))
#S.C O(m)
def canSumRevMem(nums, target,mem):
    canSumRevMem.cnt += 1
    if target == 0:
        return True
    if target < 0:
        return False
    if mem[target] != None:
        return mem[target]

    for num in nums:
        if canSumRevMem(nums,target-num,mem):
            mem[target] = True
            return True
        
    mem[target] = False
    
    return False

canSumRevMem.cnt = 0


#T.C O(n) where n is target
def canSumTab(nums, target):
    dp = [False for _ in range(target+1)]
    dp[0] = True
    for n in nums:
        dp[n] = True

    for i in range(target+1):
        canSumTab.cnt+= 1
        if dp[i]:
            for n in nums:
                if i+n <= target:
                    dp[i+n] = True
    return dp[target]

canSumTab.cnt = 0

arr = [2, 3]
targ = 500

#print(canSumRev(arr,targ), canSumRev.cnt)

mem = [None for _ in range(targ+2)]
print(canSumRevMem(arr,targ, mem), canSumRevMem.cnt)

print(canSumTab(arr, targ),canSumTab.cnt)
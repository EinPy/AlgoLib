"""
write a function that takes in a targetSum and 
and array of number as arguments. Return a bool indicating
if it's possible to generate targetSum using numbers from the array

An element can be used as many times as need
All elements are positive
"""

#initial complete search, bottom up
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
def canSumRev(nums, target):
    if target == 0:
        return True
    if target < 0:
        return False

    for num in nums:
        if canSum(nums,target-num):
            return True
    return False

#reversed with emmoization
def canSumRevMem(nums, target,mem):
    if target == 0:
        return True
    if target < 0:
        return False
    if mem[target] != None:
        return nums[target]

    for num in nums:
        mem[target] = canSum(nums,target-num)
    return mem[target]

arr = [7, 14]
targ = 300

print(canSum(arr, targ))
print(canSumRev(arr,targ))

mem = [None for _ in range(targ+2)]
print(canSumRevMem(arr,targ, mem))
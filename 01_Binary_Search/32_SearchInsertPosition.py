#Solution to https://leetcode.com/problems/search-insert-position/


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1
        mid = 0
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                
        #extra 1 added because answer is one indexed
        if target > l:
            return l + 1 + 1
        else:
            return l - 1 + 1
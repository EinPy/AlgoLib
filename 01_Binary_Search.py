# takes an anrray of numbers (nums) and a target
# and returns index of number, or -1 if not found
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

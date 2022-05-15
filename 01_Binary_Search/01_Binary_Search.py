# takes an array of numbers (nums) and a target
# and returns index of number, or -1 if not found
# note that array must be sorted

def binary_search(arr, x):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1

    return -1

#Binary search for lower bound
def lower_bound(a, x):
    l, r, m = 0, len(a), 0
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            ans = mid
            r = mid-1
        else:
            l = mid + 1
    return ans



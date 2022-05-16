"""
The array increases then decreases, O(N) is too slow
"""


#Binary search for lower bound
def lb(a, x):
    l, r, m = 0, len(a), 0
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] >= a[mid-1]:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans
"""
Somebody rotated (shifted) a sorted array.
Find the smalles element. Data is VERY big
O(n) is too slow.
"""

"""
solution
if we say true if the element is greater than arr[0]
False otherwise. First false is our solution.
"""


#Binary search for lower bound
def lower_bound(a, x):
    l, r, m = 0, len(a), 0
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if a[mid] <= a[0]:
            ans = mid
            r = mid-1
        else:
            l = mid + 1
    return ans
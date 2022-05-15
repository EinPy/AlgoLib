"""
Task: find sqrt(x) with some precision
"""


def root(x, diff):
    l, r, m = 0, x, 0

    while r - l > diff:
        mid = (r + l) // 2
        if mid * mid < x:
            l = mid
        else:
            r = mid

    return (l + r) // 2
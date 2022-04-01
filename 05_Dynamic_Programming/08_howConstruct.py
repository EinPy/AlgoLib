"""
Write a function that accepts a target string and and an
array of strings.

return an array of arrays containing all of the ways that 
target can be constructed by concatenating elements
of the array. Each element of the 2d array should
represent one combination that constructs target.

Elements may be reused any number of times.   
"""

from __future__ import annotations


def howConstruct(words, targ):
    if targ == "":
        return[]
    
    ways = []
    for w in words:
        if targ.find(w) == 0:
            suffix = targ[len(w):]
            ans = howConstruct(words, suffix)
            if ans != False:
                ways.append([w] + ans)
                
    return False

"""
Write a function that accepts a target string and and an
array of strings.

Return a boolean indicating if the word can be constructed
from the elements of the array.

Any element may be used as meny times as neccecary
"""


def canConstruct (words, target, mem = {}):
    if target in mem:
        return mem[target]
    if target == "":
        return True
    
    contains = False
    for w in words:
        if w in target:
            contains = True
    if not contains:
        return contains
        
    for w in words:
        if w in target:
            newT = target.replace(w, "")
            ans =  canConstruct(words, newT)
            mem[newT] = ans
            if ans:
                return ans
        

targ = "abcdef"
wrd = ["ab", "abc", "cd", "def", "abcd"]
print(canConstruct(wrd, targ))

            
            

    
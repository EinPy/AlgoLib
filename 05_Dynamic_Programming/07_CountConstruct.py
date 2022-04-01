"""
Write a function that accepts a target string and and an
array of strings.

return how many ways the target can be constructed by using
strings from array.

Any element may be used as meny times as neccecary
"""
#T.C if len(words) = m and targ = n
#T.C brute force O(n*m^n) S.C O(n^2)
def countConstruct(words, targ):
    if targ == "":
        return 1
    
    ways = 0
    for w in words:
        if targ.find(w) == 0:
            suffix = targ[len(w):]
            ways += countConstruct(words, suffix)
    
    return ways

#T.C (m*n^2) S.C O(m^2)
def countConstructMem(words, targ, mem = {}):
    if targ in mem:
        return mem[targ]
    if targ == "":
        return 1
    
    ways = 0
    for w in words:
        if targ.find(w) == 0:
            suffix = targ[len(w):]
            ways += countConstructMem(words, suffix, mem)
        
    mem[targ] = ways 
    return ways



print(countConstructMem(["purp","p","ur","le","purpl"],"purple"))
print(countConstructMem(
    ["e",
     "ee",
     "eee",
     "eeeeee",
     "eeeeeeee",
     "eeeeeeeeeeeeee"],
    "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"
))

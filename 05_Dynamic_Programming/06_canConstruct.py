"""
Write a function that accepts a target string and and an
array of strings.

Return a boolean indicating if the word can be constructed
from the elements of the array.

Any element may be used as meny times as neccecary
"""


"""
Note that words cannot be removed from the middle of the string
because then new ajecencys would be created

#T.C if len(words) = m and targ = n
tree is n deep and branching factor of m
T.C O(m^n) function calls. Copying string is O(n), which
will be done at every node of tree, complexity is then
T.C O(n*m^n)
Space O(m^2)
"""

def canConstruct(words, targ):
    if targ == "":
        return True
    
    for w in words:
        if targ.find(w) == 0:
            suffix = targ[len(w):]
            ans = canConstruct(words, suffix)
            if ans:
                return True
            
    return False

#with memoization
#T.C if len(words) = m and targ = n
#depth of tree n, branching factor m
#T.C O(m*n^2) S.C O(n^2)
def canConstructM(words, targ, mem):
    if mem[len(targ)] != -1: 
        return mem[len(targ)]
    if targ == "": 
        return True
    
    for w in words:
        if targ.find(w) == 0:
            suff = targ[len(w):] #suffix of the word
            if canConstructM(words, suff, mem):
                mem[len(targ)] = True
                return True
    
    mem[len(targ)] = True       
    return False
    
    
            
targ = "abcdef"
wrd = ["cd", "ab", "abc", "def", "abcd"]
targ1 = "skateboard"
wrd1 = ["bo", "rd", "ate", "t", "ska", "sk", "boar"]
#print(targ[2:])

mem = [-1 for _ in range(len(targ1)+1)]
print(canConstructM(wrd1, targ1,mem))

            

    
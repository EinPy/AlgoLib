"""
Write a function that accepts a target string and and an
array of strings.

return an array of arrays containing all of the ways that 
target can be constructed by concatenating elements
<<<<<<< HEAD
of the array. Each element of the 2d array should
represent one combination that constructs target.

Elements may be reused any number of times.   
"""

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


def howConst(words, targ):
    if targ == "":
        return [[]]

    ways = []
    for w in range(len(words)):
        if targ.find(words[w]) == 0:
            suff = targ[len(words[w]):]
            suffWays = howConst(words, suff)
            for el in suffWays:
                el.append(words[w])
                el.reverse()
            ways += suffWays
    
    return ways


#since this is a problem that requires full exploration, it can be optimized,
#but it is acutally impossible to iprove the time complexity, as the entire tree 
#will need to be checked. 
def howConstMem(words,targ, mem = {}):
    if targ in mem:
        return mem[targ]

    if targ == "":
        return [[]]

    ways = []
    for w in range(len(words)):
        if targ.find(words[w]) == 0:
            suff = targ[len(words[w]):]
            suffWays = howConstMem(words, suff,mem)
            for el in suffWays:
                el.insert(0,words[w])
            ways += suffWays
            
    mem[targ] = ways
    return ways


print(howConstMem(["he","llo","ll","o"], "hello"))
print(howConstMem(["ab", "abcde", "bcder","bc","cd","def","f","e","a","bcdef", "a", "b", "c", "d", "e", "f"],"abcdefafbcdefabcdefabcdefk"))


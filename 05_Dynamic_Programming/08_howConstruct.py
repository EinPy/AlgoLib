"""
Write a function that accepts a target string and and an
array of strings.

return a 2d array containing all of the ways that 
target can be constructed by concatenating elements
of the array. 
"""

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
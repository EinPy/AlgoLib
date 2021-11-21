#solution to: https://leetcode.com/problems/permutation-in-string/

def check_inclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    
    alph = 'abcdefghijklmnopqrstuvwxyz'
    s1_hash = {}
    s2_hash = {}
    for i in range(len(alph)):
        s1_hash[alph[i]] = 0
        s2_hash[alph[i]] = 0
        
    for i in list(s1):
        s1_hash[i] += 1
    
    p1, p2 = 0, len(s1) - 1
    for i in s2[:p2+1]:
        s2_hash[i] += 1

    
    if s1_hash == s2_hash:
        return True
        
    length = len(s2)

    while p2 < length-1:
        s2_hash[s2[p1]] -= 1
        s2_hash[s2[p2+1]] += 1
        p1 += 1
        p2 += 1
        if s1_hash == s2_hash:
            return True
        
    return False
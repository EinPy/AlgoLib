#https://leetcode.com/problems/longest-substring-without-repeating-characters/

#sliding window approach
def lengthOfLongestSubstring(s):
    left = 0
    char_set = set()
    longest = 0
    
    for right_pos, right in enumerate(s):
        while right in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(right)
        longest = max(longest, right_pos - left + 1)
        
    return longest


#slightly more efficient sliding window. but still T.C O(N)
def lengthOfLongestSubstring2(s):
    substr = ''
    longest = 0
    
    for i in s:
        if i not in substr:
            substr += i
        else:
            longest = max(longest,len(substr))
            #array starting at the position after the duplicate
            substr = substr[substr.index(i) + 1 :] + i
        
    return max(longest, len(substr))
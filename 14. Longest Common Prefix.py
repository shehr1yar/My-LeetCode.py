class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""        
        for index in range(len(strs[0])):
            for word in strs:
                if index == len(word) or word[index] != strs[0][index]:
                    return prefix
            prefix += strs[0][index]        
        return prefix

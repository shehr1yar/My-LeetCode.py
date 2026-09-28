class Solution(object):
    def twoSum(self, nums, target):
        nd = {}     # nd = numbers dictionary
        
        for i, num in enumerate(nums):
            c = target - num    # c = complement 
            if c in nd:
                return [nd[c], i]
            nd[num] = i

class Solution(object):
    def threeSum(self, nums):
        triplets = []
        nums.sort()
        
        for idx, val in enumerate(nums):
            # skip duplicate values for the first element
            if idx > 0 and val == nums[idx - 1]:
                continue
                
            left, right = idx + 1, len(nums) - 1
            while left < right:
                current_sum = val + nums[left] + nums[right]
                
                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    triplets.append([val, nums[left], nums[right]])
                    left += 1
                    # skip duplicate values for the second element
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                        
        return triplets

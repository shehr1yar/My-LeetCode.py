class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        results, current_quad = [], []
        
        def kSum(k, start, target):
            if k != 2:
                for idx in range(start, len(nums) - k + 1):
                    if idx > start and nums[idx] == nums[idx - 1]:
                        continue
                    current_quad.append(nums[idx])
                    kSum(k - 1, idx + 1, target - nums[idx])
                    current_quad.pop()
                return
            
            # base case, two sum II
            left, right = start, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    results.append(current_quad + [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
        kSum(4, 0, target)
        return results

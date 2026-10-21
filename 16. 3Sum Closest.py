class Solution(object):
    def threeSumClosest(self, nums, target):
        
        nums.sort()
        length = len(nums)
        best_sum = float('inf')
        
        for idx in range(length):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            
            left, right = idx + 1, length - 1
            while left < right:
                total = nums[idx] + nums[left] + nums[right]
                
                if abs(total - target) < abs(best_sum - target):
                    best_sum = total
                
                if total == target:
                    return total
                elif total < target:
                    left += 1
                else:
                    right -= 1
                    
        return best_sum

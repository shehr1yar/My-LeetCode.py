class Solution(object):
    def maxArea(self, height):

        # BRUTE FORCE 
        # max_water = 0 
        # 
        # for left_idx in range(len(height)): 
        #     for right_idx in range(left_idx + 1, len(height)): 
        #         current_area = (right_idx - left_idx) * min(height[left_idx], height[right_idx]) 
        #         max_water = max(max_water, current_area) 
        # 
        # return max_water 

        max_water = 0
        left_ptr, right_ptr = 0, len(height) - 1
        
        while left_ptr < right_ptr:
            current_area = (right_ptr - left_ptr) * min(height[left_ptr], height[right_ptr])
            max_water = max(max_water, current_area)
            
            if height[left_ptr] < height[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1
                
        return max_water

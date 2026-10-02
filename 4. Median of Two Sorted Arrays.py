class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        small_arr, large_arr = nums1, nums2
        combined_size = len(nums1) + len(nums2)
        half_boundary = combined_size // 2
        
        # Ensure small_arr is always the shorter array
        if len(large_arr) < len(small_arr):
            small_arr, large_arr = large_arr, small_arr
        
        # Binary search range on the smaller array
        low, high = 0, len(small_arr) - 1
        
        while True:
            idx1 = (low + high) // 2 
            idx2 = half_boundary - idx1 - 2 
            
            # Boundary values for small_arr partition
            left_max1 = small_arr[idx1] if idx1 >= 0 else float("-inf")
            right_min1 = small_arr[idx1 + 1] if (idx1 + 1) < len(small_arr) else float("inf")
            
            # Boundary values for large_arr partition
            left_max2 = large_arr[idx2] if idx2 >= 0 else float("-inf")
            right_min2 = large_arr[idx2 + 1] if (idx2 + 1) < len(large_arr) else float("inf")
            
            # Check if partition boundaries match correctly
            if left_max1 <= right_min2 and left_max2 <= right_min1:
                # Odd total length handling
                if combined_size % 2:
                    return min(right_min1, right_min2)
                # Even total length handling
                return (max(left_max1, left_max2) + min(right_min1, right_min2)) / 2.0
                
            elif left_max1 > right_min2:
                high = idx1 - 1
            else:
                low = idx1 + 1

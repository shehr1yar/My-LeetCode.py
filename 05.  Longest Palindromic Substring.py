class Solution(object):
    def longestPalindrome(self, s):
        longest_sub = ""
        max_length = 0
        
        for idx in range(len(s)):
            # Check for odd length palindromes
            left_ptr, right_ptr = idx, idx
            while left_ptr >= 0 and right_ptr < len(s) and s[left_ptr] == s[right_ptr]:
                if (right_ptr - left_ptr + 1) > max_length:
                    longest_sub = s[left_ptr:right_ptr+1]
                    max_length = right_ptr - left_ptr + 1
                left_ptr -= 1
                right_ptr += 1
                
            # Check for even length palindromes
            left_ptr, right_ptr = idx, idx + 1
            while left_ptr >= 0 and right_ptr < len(s) and s[left_ptr] == s[right_ptr]:
                if (right_ptr - left_ptr + 1) > max_length:
                    longest_sub = s[left_ptr:right_ptr+1]
                    max_length = right_ptr - left_ptr + 1
                left_ptr -= 1
                right_ptr += 1
                
        return longest_sub

class Solution(object):
    def romanToInt(self, s):
        # largest to smallest: add them up
        # smaller before larger: subtract smaller
        
        num_map = { "I" : 1, "V" : 5, "X" : 10,
                    "L" : 50, "C" : 100, "D" : 500, "M" : 1000 }
        total_value = 0
        
        for idx in range(len(s)):
            if idx + 1 < len(s) and num_map[s[idx]] < num_map[s[idx + 1]]:
                total_value -= num_map[s[idx]]
            else:
                total_value += num_map[s[idx]]
                
        return total_value

class Solution(object):
    def isMatch(self, s, p):
        # Top-down memoization approach
        memo = {}
        
        def solve(idx_s, idx_p):
            if (idx_s, idx_p) in memo:
                return memo[(idx_s, idx_p)]
                
            if idx_s >= len(s) and idx_p >= len(p):
                return True
                
            if idx_p >= len(p):
                return False
                
            is_char_match = idx_s < len(s) and (s[idx_s] == p[idx_p] or p[idx_p] == ".")
            
            if (idx_p + 1) < len(p) and p[idx_p + 1] == "*":
                memo[(idx_s, idx_p)] = (solve(idx_s, idx_p + 2) or
                                        (is_char_match and solve(idx_s + 1, idx_p)))
                return memo[(idx_s, idx_p)]
                
            if is_char_match:
                memo[(idx_s, idx_p)] = solve(idx_s + 1, idx_p + 1)
                return memo[(idx_s, idx_p)]
                
            memo[(idx_s, idx_p)] = False
            return False
            
        return solve(0, 0)

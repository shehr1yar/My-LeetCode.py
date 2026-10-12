class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1: 
            return s
        
        result_str = ""
        for row in range(numRows):
            stride = 2 * (numRows - 1)
            
            for idx in range(row, len(s), stride):
                result_str += s[idx]
                
                if (0 < row < numRows - 1 and 
                    idx + stride - 2 * row < len(s)):
                    result_str += s[idx + stride - 2 * row]
                    
        return result_str

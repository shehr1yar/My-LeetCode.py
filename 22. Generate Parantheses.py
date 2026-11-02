class Solution(object):
    def generateParenthesis(self, n):
        
        current_path = []
        output_list = []
        
        def helper(openN, closedN):
            if openN == closedN == n:
                output_list.append("".join(current_path))
                return
            
            if openN < n:
                current_path.append("(")
                helper(openN + 1, closedN)
                current_path.pop()
                
            if closedN < openN:
                current_path.append(")")
                helper(openN, closedN + 1)
                current_path.pop()
                
        helper(0, 0)
        return output_list

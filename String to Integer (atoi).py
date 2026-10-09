class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0
        
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        polarity = 1
        total_value = 0
        
        # handle optional sign
        if s[0] == '-':
            polarity = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        # process digits
        for symbol in s:
            if not symbol.isdigit():
                break
            
            digit = int(symbol)
            
            # check overflow
            if total_value > INT_MAX // 10 or (total_value == INT_MAX // 10 and digit > 7):
                return INT_MAX if polarity == 1 else INT_MIN
            
            total_value = total_value * 10 + digit
        
        return total_value * polarity

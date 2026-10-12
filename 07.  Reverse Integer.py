class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_val = 0

        while x:
            curr_digit = x % 10
            x //= 10
            if reversed_val > 214748364 or (reversed_val == 214748364 and curr_digit > 7):
                return 0

            reversed_val = reversed_val * 10 + curr_digit

        return reversed_val * sign

class Solution(object):
    def intToRoman(self, num):
        roman_mapping = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9],
                         ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
                         ["C", 100], ["CD", 400], ["D", 500], ["CM", 900],
                         ["M", 1000]]

        final_string = ""

        for roman_char, unit_value in reversed(roman_mapping):
            if num // unit_value:
                repeat_factor = num // unit_value
                final_string += (roman_char * repeat_factor)
                num = num % unit_value
                
        return final_string

class Solution(object):
    def letterCombinations(self, digits):
        output_list = []
        phone_mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                output_list.append(curStr)
                return
            for letter in phone_mapping[digits[i]]:
                backtrack(i + 1, curStr + letter)

        if digits:
            backtrack(0, "")

        return output_list

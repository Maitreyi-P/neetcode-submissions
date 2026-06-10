class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []

        digmap = {
            "2":"abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def bk(i,curr):
            if len(curr) == len(digits):
                res.append(curr)
                return

            for c in digmap[digits[i]]:
                bk(i+1, curr+c)
            
        if digits:
            bk(0,"")

        return res
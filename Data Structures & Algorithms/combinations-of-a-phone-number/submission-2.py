class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        alpha = {
            "2" : list("abc"),
            "3" : list("def"),
            "4" : list("ghi"),
            "5" : list("jkl"),
            "6" : list("mno"),
            "7" : list("pqrs"),
            "8" : list("tuv"),
            "9" : list("wxyz"),
        }
        res = []
        if not digits:
            return res
        def bt(curr, pos):
            nonlocal res
            if pos == len(digits):
                res.append(curr)
                return
            
            for c in alpha[digits[pos]]:
                bt(curr + c, pos + 1)
        bt("", 0)
        return res

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        conv = { "2" : tuple("abc") , "3" : tuple("def"), "4" : tuple("ghi"), "5" : tuple("jkl"), "6" : tuple("mno"), "7" : tuple("pqrs"), "8" : tuple("tuv"), "9" : tuple("wxyz") }

        def bt(i, subs):
            if i >= len(digits):
                res.append("".join(subs))
                return 

            for c in conv[digits[i]]:
                subs.append(c)
                bt(i + 1, subs)
                subs.pop()
        bt(0, [])
        return res
            

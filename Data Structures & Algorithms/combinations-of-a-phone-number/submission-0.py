class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        conv = { "2" : tuple("abc") , "3" : tuple("def"), "4" : tuple("ghi"), "5" : tuple("jkl"), "6" : tuple("mno"), "7" : tuple("pqrs"), "8" : tuple("tuv"), "9" : tuple("wxyz") }
        res = []
        if digits == "":
            return res

        def dfs(i, sub):
            if i >= len(digits):
                res.append("".join(sub.copy()))
                return
            
            for c in conv[digits[i]]:
                sub.append(c)
                dfs(i + 1, sub)
                sub.pop()
        
        dfs(0, [])
        return res
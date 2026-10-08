class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True


        res = []
        part = []
        def bt(i):
            nonlocal res
            if i == len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    part.append(s[i: j + 1])
                    bt(j + 1)
                    part.pop()
        bt(0)
        return res


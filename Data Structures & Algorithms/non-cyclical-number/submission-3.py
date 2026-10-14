class Solution:
    def isHappy(self, n: int) -> bool:
        sn = set()
        def sum_square(n):
            res = 0
            while n > 0:
                res += (n % 10) ** 2
                n //= 10
            return res
        
        curr = n
        while curr not in sn and curr != 1:
            sn.add(curr)
            curr = sum_square(curr)

        return curr == 1
        

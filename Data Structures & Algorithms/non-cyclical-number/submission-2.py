class Solution:
    def isHappy(self, n: int) -> bool:
        sn = set()
        nn = 0
        while n != 1:
            if n in sn:
                return False
            sn.add(n)
            nn = 0
            while n > 0:
                nn += (n % 10) ** 2
                n //= 10
            n = nn
        return True
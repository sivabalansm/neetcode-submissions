class Solution:
    def isHappy(self, n: int) -> bool:
        sn = set()

        while n != 1:
            d = 0
            while n > 0:
                d += (n % 10) ** 2
                n = n // 10
            if d == 1:
                return True
            elif d in sn:
                return False
            else:
                sn.add(d)
                n = d
        return True
        

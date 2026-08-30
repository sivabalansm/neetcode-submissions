class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: 
            return 0

        def helper(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            res = helper(x, n // 2)
            po = res * res
            return po * x if n % 2 == 1 else po
        
        res = helper(abs(x), abs(n))
        if x < 0:
            res = res if abs(n) % 2 == 0 else -res
        return 1/res if n < 0 else res
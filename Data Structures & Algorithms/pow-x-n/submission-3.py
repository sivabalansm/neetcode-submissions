class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        if n < 0:
            n *= -1
            return 1/(float(x * self.myPow(x, n - 1)))
        return float(x * self.myPow(x, n - 1))
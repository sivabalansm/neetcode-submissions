class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_square(n):
            res = 0
            while n > 0:
                res += (n % 10) ** 2
                n //= 10
            return res
        
        slow, fast = n, sum_square(n)
        while slow != fast:
            fast = sum_square(fast)
            fast = sum_square(fast)
            slow = sum_square(slow)

        return fast == 1
        

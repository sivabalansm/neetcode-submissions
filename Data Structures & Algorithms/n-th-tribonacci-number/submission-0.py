class Solution:
    def tribonacci(self, n: int) -> int:
        zero = 0
        one = 1
        two = 1
        if n == 0:
            return zero
        elif n <= 2:
            return one
        else:
            for _ in range(n - 2):
                three = zero + one + two
                two, one, zero = three, two, one
            return two



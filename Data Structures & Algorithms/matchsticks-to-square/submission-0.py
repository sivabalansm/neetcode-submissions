class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        p = sum(matchsticks)
        if p % 4 != 0:
            return False

        n = len(matchsticks)

        l = p // 4
        sides = [0] * 4

        def bt(i):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]
            
            for side in range(4):
                sides[side] += matchsticks[i]
                if bt(i + 1):
                    return True
                sides[side] -= matchsticks[i]

            return False
        return bt(0)
            

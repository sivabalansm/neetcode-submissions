class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        p = sum(matchsticks)
        if p % 4 != 0:
            return False

        n = len(matchsticks)
        matchsticks.sort(reverse=True)
        l = p // 4
        sides = [0] * 4

        def bt(i):
            if i == len(matchsticks):
                return True
            
            for side in range(4):
                if sides[side] + matchsticks[i] <= l:
                    sides[side] += matchsticks[i]
                    if bt(i + 1):
                        return True
                    sides[side] -= matchsticks[i]

                if sides[side] == 0:
                    break

            return False
        return bt(0)
            

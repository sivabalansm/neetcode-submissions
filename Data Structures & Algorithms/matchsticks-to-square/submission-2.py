"""
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
            
"""
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False

        length = total_length // 4
        sides = [0] * 4
        matchsticks.sort(reverse=True)

        def dfs(i):
            if i == len(matchsticks):
                return True

            for side in range(4):
                if sides[side] + matchsticks[i] <= length:
                    sides[side] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[side] -= matchsticks[i]

                if sides[side] == 0:
                    break

            return False

        return dfs(0)
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}
        def dfs(i, alice = True):
            if i >= len(stoneValue):
                return 0
            if (i, alice) in dp:
                return dp[(i, alice)]
            res = 0 if alice else float("inf")
            total = 0
            for j in range(3):
                if i + j == len(stoneValue):
                    break
                total += stoneValue[i + j]
                if alice:
                    res = max(res, total + dfs(i + j + 1, not alice))
                else:
                    res = min(res, dfs(i + j + 1, not alice))
            dp[(i, alice)] = res
            return res

        s = sum(stoneValue)
        alice = dfs(0)
        print(alice)
        bob = s - alice

        if alice > bob:
            return "Alice"
        elif bob > alice:
            return "Bob"
        else:
            return "Tie"


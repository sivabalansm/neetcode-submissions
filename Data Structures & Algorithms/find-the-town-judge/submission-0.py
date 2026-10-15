class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        is_trusting = [False] * (n + 1)

        for src, dst in trust:
            is_trusting[src] = True
        
        for nei in range(1, n + 1):
            if not is_trusting[nei]:
                return nei
        return -1
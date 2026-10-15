class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        is_trusting = [False] * (n + 1)

        for src, dst in trust:
            is_trusting[src] = True
        print(is_trusting)
        judge = 0
        for nei in range(1, n + 1):
            if judge > 0 and not is_trusting[nei]:
                return -1

            if not is_trusting[nei]:
                judge = nei
        
        is_trusting_judge = [False] * (n + 1)
        is_trusting_judge[judge] = True
        for src, dst in trust:
            if not is_trusting_judge[src] and dst == judge:
                is_trusting_judge[src] = True
        print(is_trusting_judge)
        return judge if all(is_trusting_judge[1:]) else -1

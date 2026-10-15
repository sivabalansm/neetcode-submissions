class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = defaultdict(int)

        for src, dst in trust:
            delta[src] -= 1
            delta[dst] += 1
        
        for ppl in delta:
            if delta[ppl] == n - 1:
                return ppl
        return -1
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ls = defaultdict(int)

        for np, fro, to in trips:
            ls[fro] += np
            ls[to] -= np
        
        cap = 0
        for p in sorted(ls.keys()):
            cap += ls[p]
            if cap > capacity:
                return False
        return True

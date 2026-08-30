class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = set()

        x, y, z = target
        for t in triplets:
            if t[0] > x or t[1] > y or t[2] > z:
                continue
            
            for i, v in enumerate(target):
                if v == t[i]:
                    res.add(i)
        return len(res) == 3
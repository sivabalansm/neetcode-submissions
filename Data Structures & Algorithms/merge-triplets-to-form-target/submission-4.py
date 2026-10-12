class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        poss = [0] * 3
        tx, ty, tz = target
        for x, y, z in triplets:
            if x > tx or y > ty or z > tz:
                continue
            poss[0] = max(poss[0], x)
            poss[1] = max(poss[1], y)
            poss[2] = max(poss[2], z)
        
        return poss == target

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        got = set()
        
        x, y, z = target
        for t in triplets:
            if t[0] > x or t[1] > y or t[2] > z:
                continue
            
            for i in range(3):
                if t[i] == target[i]:
                    got.add(i)
        return len(got) == 3
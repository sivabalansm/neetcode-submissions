class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, v):
        while self.parents[v] != v:
            v = self.parents[v]
        return v
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        
        if self.rank[pu] > self.rank[pv]:
            self.parents[pv] = pu
            self.rank[pu] += self.rank[pv]
        else:
            self.parents[pu] = pv
            self.rank[pv] += self.rank[pu]

        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                n1 = nums[i]
                n2 = nums[j]
                if math.gcd(n1, n2) > 1:
                    uf.union(i, j)
        
        if max(uf.rank) == len(nums):
            return True
        return False

        
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, v):
        while self.parent[v] != v:
            v = self.parent[v]
        return v
    
    def union(self, v, u):
        pv, pu = self.find(v), self.find(u)

        if pv == pu:
            return False
        
        if self.rank[pv] > self.rank[pu]:
            self.rank[pv] += self.rank[pu]
            self.parent[pu] = pv
        else:
            self.rank[pu] += self.rank[pv]
            self.parent[pv] = pu

        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i)
        
        edges.sort(key=lambda e : e[2]) # weight

        mst_weight = 0
        uf = UnionFind(n)
        for u, v, w, i in edges:
            if uf.union(u, v):
                mst_weight += w
        
        critical, pseudo = [], []
        for u, v, w, i in edges:
            # critical edges
            weight = 0
            uf = UnionFind(n)
            for n1, n2, edge_weight, j in edges:
                if i != j and uf.union(n1, n2):
                    weight += edge_weight
            
            if max(uf.rank) != n or weight > mst_weight:
                critical.append(i)
                continue
            
            # pseudo critical
            uf = UnionFind(n)
            uf.union(u, v)
            weight = w
            for n1, n2, edge_weight, j in edges:
                if uf.union(n1, n2):
                    weight += edge_weight
            
            if weight == mst_weight:
                pseudo.append(i)
        return [critical, pseudo]





        
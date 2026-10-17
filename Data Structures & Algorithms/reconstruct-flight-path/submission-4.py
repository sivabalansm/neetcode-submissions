class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for fro, to in tickets:
            adj[fro].append(to)
        
        for fro in adj:
            adj[fro].sort(reverse=True)
        
        res = []
        def dfs(node):
            res.append(node)
            if adj[node]:
                dfs(adj[node].pop())
        dfs("JFK")
        return res
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for fro, to in sorted(tickets)[::-1]:
            adj[fro].append(to)
        res = []
        def dfs(node):
            while adj[node]:
                dst = adj[node].pop()
                dfs(dst)
            res.append(node)
        dfs("JFK")
        return res[::-1]
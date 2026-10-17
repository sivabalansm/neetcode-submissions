class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for fro, to in tickets:
            adj[fro].append(to)
        #print(sorted(tickets, reverse=True))
        for fro in adj:
            adj[fro].sort(reverse=True)
        res = []
        def dfs(node):
            while adj[node]:
                dfs(adj[node].pop())
            res.append(node)
        dfs("JFK")
        print(res)
        return res[::-1]
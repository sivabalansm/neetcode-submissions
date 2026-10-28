class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        res = []
        adj = defaultdict(set)
        indegree = {}
        for word in words:
            for c in word:
                indegree[c] = 0
        for i in range(1, len(words)):
            w1 = words[i - 1]
            w2 = words[i]

            wlen = min(len(w1), len(w2))
            p = 0
            while p < wlen and w1[p] == w2[p]:
                p += 1
            if p == wlen and len(w1) > len(w2):
                return ""
            elif p == wlen:
                continue

            if w2[p] not in adj[w1[p]]:
                adj[w1[p]].add(w2[p])
                indegree[w2[p]] += 1
        q = deque([c for c in indegree if indegree[c] == 0])

        while q:
            c = q.popleft()
            res.append(c)

            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return "".join(res) 
        
            

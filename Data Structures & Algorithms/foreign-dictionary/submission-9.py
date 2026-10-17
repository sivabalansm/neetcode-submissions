class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        res = []
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}

        for i in range(1, len(words)):
            w1 = words[i - 1]
            w2 = words[i]
            wlen = min(len(w1), len(w2))
            idx = 0
            while idx < wlen and w1[idx] == w2[idx]:
                idx += 1
            if len(w1) > len(w2) and w1[:wlen] == w2[:wlen]:
                return ""

            if idx < wlen and w2[idx] not in adj[w1[idx]]:
                adj[w1[idx]].add(w2[idx])
                indegree[w2[idx]] += 1


        q = deque([l for l in indegree if indegree[l] == 0])
        res = ""
        while q:
            l = q.popleft()
            res += l
            for nei in adj[l]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(res) != len(indegree):
            return ""
        return res 

            


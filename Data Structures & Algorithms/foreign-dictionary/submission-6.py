class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        res = []
        adj = defaultdict(list)
        indegree = defaultdict(int)

        for i in range(1, len(words)):
            w1 = words[i - 1]
            w2 = words[i]
            wlen = min(len(w1), len(w2))
            idx = 0
            while idx < wlen and w1[idx] == w2[idx]:
                idx += 1
            if idx == wlen and len(w1) > len(w2):
                return ""
            print(idx, wlen, w1, w2)
            adj[w1[idx]].append(w2[idx])
            indegree[w2[idx]] += 1

        residual = set()
        for word in words:
            for c in word:
                if c not in adj and c not in indegree:
                    residual.add(c)

        q = deque([l for l in adj if indegree[l] == 0])
        res = ""
        while q:
            l = q.popleft()
            res += l
            for nei in adj[l]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res + "".join(residual)

            


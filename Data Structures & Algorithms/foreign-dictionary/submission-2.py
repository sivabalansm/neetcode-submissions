class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c : set() for w in words for c in w}
        indegree = { c : 0 for c in adj }

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    c1 = w1[j]
                    c2 = w2[j]
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indegree[c2] += 1
                    break
        
        q = deque([c for c in adj if indegree[c] == 0])
        res = ""
        print(adj)
        while q:
            qlen = len(q)
            for i in range(qlen):
                c = q.popleft()
                res += c
                for nc in adj[c]:
                    indegree[nc] -= 1
                    if indegree[nc] == 0:
                        q.append(nc)
        return res


        

        

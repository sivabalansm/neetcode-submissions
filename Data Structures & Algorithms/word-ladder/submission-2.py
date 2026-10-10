class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        
        patadj = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                patadj[pattern].append(word)
        
        visit = set()
        q = deque([beginWord])
        res = 1
        while q:
            qlen = len(q)
            for i in range(qlen):
                w = q.popleft()
                if w == endWord:
                    return res
                if w in visit:
                    continue
                visit.add(w)
                for i in range(len(w)):
                    pattern = w[:i] + "*" + w[i + 1:]
                    for nei in patadj[pattern]:
                        q.append(nei)
            res += 1
        return res
        
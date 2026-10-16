class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        print(wordList)
        wordList.append(beginWord)
        adj = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pat = word[:i] + "*" + word[i+1:]
                adj[pat].append(word)
        print(adj)
        res = 1
        q = deque([beginWord])
        visit = set()
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                visit.add(word)
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pat = word[:i] + "*" + word[i + 1:]
                    for nei in adj[pat]:
                        if nei not in visit:
                            q.append(nei)

            res += 1
        return 0


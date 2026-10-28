class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pat = word[:i] + "*" + word[i + 1:]
                adj[pat].append(word)
        print(adj)
        sn = set()
        q = deque([beginWord])
        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                word = q.popleft()
                print(word)
                sn.add(word)
                if word == endWord:
                    return steps
                for i in range(len(word)):
                    pat = word[:i] + "*" + word[i + 1:]
                    for next_word in adj[pat]:
                        if next_word not in sn:
                            q.append(next_word)
                            sn.add(next_word)
        return 0



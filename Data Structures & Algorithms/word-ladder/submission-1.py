class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        def similar_word(w1, w2) -> bool:
            l = 0
            r = len(w1) - 1
            if len(w1) != len(w2):
                return False
            difference_safe = True
            while l <= r:
                if w1[l] == w2[l] and w1[r] == w2[r]:
                    l += 1
                    r -= 1
                elif difference_safe:
                    difference_safe = False
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        adj = defaultdict(list)
        for word in wordList:
            """
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
        res = 0
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
                    pattern = w[:i] + "*" + word[i + 1:]
                    for nei in patadj[pattern]:
                        q.append(nei)
            res += 1
        return res




        
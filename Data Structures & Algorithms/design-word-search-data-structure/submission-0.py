class Tree:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:
    def __init__(self):
        self.root = Tree()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Tree()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        self.res = False
        def dfs(i, curr):
            if i >= len(word):
                if not self.res:
                    self.res = curr.end
                return
            c = word[i]
            if c == ".":
                for k in curr.children:
                    dfs(i + 1, curr.children[k])
            elif c in curr.children:
                dfs(i + 1, curr.children[c])
        dfs(0, curr)
        return self.res



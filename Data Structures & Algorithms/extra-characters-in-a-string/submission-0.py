class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]

        curr.end = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        res = len(s)

        curr = trie.root 
        i = 0
        size = 0
        while i < len(s) and s[i] in curr.children:
            c = s[i]
            if c in curr.children:
                size += 1
                curr = curr.children[c]
                if curr.end:
                    res -= size
                    size = 0
            else:
                curr = trie.root
                size = 0
            i += 1
        return res







        
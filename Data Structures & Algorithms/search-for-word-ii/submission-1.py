class TreeNode():
    def __init__(self):
        self.children = {}
        self.end = False
        self.idx = -1

class Trie:
    def __init__(self):
        self.root = TreeNode()
    
    def addWord(self, word, idx):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode()
            curr = curr.children[c]
        curr.end = True
        curr.idx = idx
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for i in range(len(words)):
            w = words[i]
            trie.addWord(w, i)
        
        R = len(board)
        C = len(board[0])
        res = []
        visit = set()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(curr, r, c):
            nonlocal res
            if curr.end and curr.idx != -1:
                res.append(words[curr.idx])
                curr.idx = -1
                return
            if r >= R or r < 0 or c >= C or c < 0 or (r, c) in visit or board[r][c] not in curr.children:
                return

            visit.add((r, c))
            for dr, dc in dirs:
                dfs(curr.children[board[r][c]], r + dr, c + dc)
            visit.remove((r, c))
        for r in range(R):
            for c in range(C):
                dfs(trie.root, r, c)
        return res



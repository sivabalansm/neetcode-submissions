class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))

        res = set()
        trie = Trie()
        for word in words:
            trie.insert(word)

        def bt(r, c, curr, word):
            if curr.end:
                res.add("".join(word))

            if r >= ROWS or c >= COLS or r < 0 or c < 0 or board[r][c] == "#":
                return

            if board[r][c] in curr.children:
                curr = curr.children[board[r][c]]
                word.append(board[r][c])
                board[r][c] = "#"
                for dr, dc in dirs:
                    bt(r + dr, c + dc, curr, word)
                board[r][c] = word.pop()
        for r in range(ROWS):
            for c in range(COLS):
                bt(r, c, trie.root, [])
        return list(res)


            
            
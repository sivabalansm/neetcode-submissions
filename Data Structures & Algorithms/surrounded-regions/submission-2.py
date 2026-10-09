class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        R = len(board)
        C = len(board[0])
        bordered = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r >= R or c >= C or board[r][c] == "X" or (r, c) in bordered:
                return 
            
            bordered.add((r, c))
            for dr, dc in dirs:
                dfs(r + dr, c + dc)
        
        for c in range(C):
            dfs(0, c)
            dfs(R - 1, c)

        for r in range(R):
            dfs(r, 0)
            dfs(r, C - 1)
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O" and (r, c) not in bordered:
                    board[r][c] = "X"

                

                

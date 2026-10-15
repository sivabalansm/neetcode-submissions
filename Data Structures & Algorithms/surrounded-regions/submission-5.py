class Solution:
    def solve(self, board: List[List[str]]) -> None:
        grid = board
        R = len(board)
        C = len(board[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == "X" or grid[r][c] == "T":
                return
            
            grid[r][c] = "T"
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
                if grid[r][c] == "O":
                    grid[r][c] = "X"
                elif grid[r][c] == "T":
                    grid[r][c] = "O"
        
        


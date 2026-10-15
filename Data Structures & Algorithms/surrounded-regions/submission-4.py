class Solution:
    def solve(self, board: List[List[str]]) -> None:
        grid = board
        R = len(board)
        C = len(board[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C:
                return True
            if grid[r][c] == "X" or grid[r][c] == "T":
                return False
                
            grid[r][c] = "T"
            for dr, dc in dirs:
                if dfs(r + dr, c + dc):
                    grid[r][c] = "#"
                    return True

            grid[r][c] = "X"
            return False
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "O":
                    dfs(r, c)
                if grid[r][c] == "#":
                    grid[r][c] = "O"
        
        


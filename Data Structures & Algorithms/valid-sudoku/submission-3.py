class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        square = [set() for _ in range(9)]


        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                if num in cols[c] or num in rows[r] or num in square[(r // 3) * 3 + c // 3]:
                    return False
                
                cols[c].add(num)
                rows[r].add(num)
                square[(r// 3) * 3 + c // 3].add(num)
        return True

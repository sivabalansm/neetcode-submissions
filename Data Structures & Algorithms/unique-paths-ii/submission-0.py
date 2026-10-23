class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        if obstacleGrid[n - 1][m - 1] == 1:
            return 0

        for r in range(n):
            for c in range(m):
                obstacleGrid[r][c] *= -1

        obstacleGrid[n - 1][m - 1] = 1

        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                if obstacleGrid[r][c] == -1:
                    obstacleGrid[r][c] = 0
                    continue
                
                if r + 1 < n:
                    obstacleGrid[r][c] += obstacleGrid[r + 1][c] 
                if c + 1 < m:
                    obstacleGrid[r][c] += obstacleGrid[r][c + 1]
        
        return obstacleGrid[0][0]
                

                


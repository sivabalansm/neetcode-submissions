"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(n, r, c):
            if n == 1:
                return Node(grid[r][c] == 1, True)
            half = n // 2
            topLeft = dfs(half, r, c)
            topRight = dfs(half, r, c + half)
            bottomLeft = dfs(half, r + half, c)
            bottomRight = dfs(half, r + half, c + half)

            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                return Node(topLeft.val, True)
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(len(grid), 0, 0)

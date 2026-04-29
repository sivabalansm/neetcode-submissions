"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cre = {}

        def dfs(node):
            if node.val in cre:
                return cre[node.val]

            cre[node.val] = Node(node.val)
            
            for n in node.neighbors:
                cre[node.val].neighbors.append(dfs(n))
            return cre[node.val]
        return dfs(node)

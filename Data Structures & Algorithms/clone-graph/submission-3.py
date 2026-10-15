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

        clones = {}

        def dfs(node):
            if not node:
                return None
            if node.val not in clones:
                clones[node.val] = Node(node.val)

            clone = clones[node.val]

            for nei in node.neighbors:
                if nei.val in clones:
                    clone.neighbors.append(clones[nei.val])
                else:
                    clone.neighbors.append(dfs(nei))
            
            return clone

        return dfs(node)




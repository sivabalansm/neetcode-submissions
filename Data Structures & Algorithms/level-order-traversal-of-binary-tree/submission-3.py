# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        q = deque() 
        q.append(root) 
        res = [[root.val]]

        while q:
            lq = len(q)
            for _ in range(lq):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if q:
                res.append([nn.val for nn in q])
        return res
            
            


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        q = deque([root])
        res = []
        while q:
            last = float('inf')
            for i in range(len(q)):
                n = q.popleft()
                last = n.val

                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            if last != float('inf'):
                res.append(last)
        return res

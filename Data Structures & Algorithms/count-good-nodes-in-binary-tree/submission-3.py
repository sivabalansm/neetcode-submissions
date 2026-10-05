# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        q = deque([(root, root.val - 1)])
        while q:
            ql = len(q)
            for i in range(ql):
                n, mv = q.popleft()
                if n.val >= mv:
                    res += 1
                
                if n.left:
                    q.append((n.left, max(mv, n.val)))
                if n.right:
                    q.append((n.right, max(mv, n.val)))
        return res
                
            


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        st = [[root, 1]]
        res = 0

        while st:
            n, d = st.pop()

            if n:
                res = max(res, d)
                st.append([n.left, d + 1])
                st.append([n.right, d + 1])
        return res
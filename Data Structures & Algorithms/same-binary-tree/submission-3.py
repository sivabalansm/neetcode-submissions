# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            np = q1.popleft()
            nq = q2.popleft()

            if not np and not nq:
                continue
            
            if not np or not nq or np.val != nq.val:
                return False
            
            q1.append(np.left)
            q1.append(np.right)
            q2.append(nq.left)
            q2.append(nq.right)
        return True
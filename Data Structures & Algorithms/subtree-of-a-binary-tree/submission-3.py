# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and not subRoot or subRoot and not root:
            return False

        def isSameTree(n1, n2):
            q1 = deque([n1])
            q2 = deque([n2])

            while q1 and q2:
                n1 = q1.popleft()
                n2 = q2.popleft()

                if not n1 and not n2:
                    continue
                
                if not n1 or not n2 or n1.val != n2.val:
                    return False
                
                q1.append(n1.left)
                q1.append(n1.right)
                q2.append(n2.left)
                q2.append(n2.right)
            return True
        
        q = deque([root])

        while q:
            n = q.popleft()

            if not n:
                continue

            if n.val == subRoot.val and isSameTree(n, subRoot):
                return True
            
            q.append(n.left)
            q.append(n.right)
        return False
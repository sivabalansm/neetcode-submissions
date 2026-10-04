from collections import defaultdict
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        copy = defaultdict(lambda : Node(0))

        curr = head
        while curr:
            n = copy[curr]
            n.val = curr.val
            n.random = copy[curr.random] if curr.random else None
            n.next = copy[curr.next] if curr.next else None
            curr = curr.next
        
        return copy[head]


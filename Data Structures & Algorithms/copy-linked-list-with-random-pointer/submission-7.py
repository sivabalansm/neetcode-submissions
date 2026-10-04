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
        copy = defaultdict(lambda : Node(0))
        copy[None] = None
        curr = head
        while curr:
            n = copy[curr]
            n.val = curr.val
            n.random = copy[curr.random] 
            n.next = copy[curr.next] 
            curr = curr.next
        
        return copy[head]


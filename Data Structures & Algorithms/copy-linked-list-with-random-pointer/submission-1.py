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
        matching = {}
        curr = head
        while curr:
            matching[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            corr = matching[curr]
            if curr.next:
                corr.next = matching[curr.next]
            if curr.random:
                corr.random = matching[curr.random]
            curr = curr.next

        return matching[head]
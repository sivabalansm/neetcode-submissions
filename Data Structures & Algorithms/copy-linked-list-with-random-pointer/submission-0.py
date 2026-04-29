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
        l = {None : None}
        copy = Node(0, None)
        ch = head
        cc = copy
        while ch:
            new_copy = Node(ch.val)
            cc.next = new_copy
            l[ch] = new_copy
            cc = cc.next
            ch = ch.next
        
        ch = head
        cc = copy.next
        while ch and cc:
            cc.random = l[ch.random]
            ch = ch.next
            cc = cc.next

        return copy.next
            
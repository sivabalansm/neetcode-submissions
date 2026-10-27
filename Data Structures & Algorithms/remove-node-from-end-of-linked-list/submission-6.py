# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
S, 1, 2, 3, 4, N
      s        e
   sz = 0
S, 1, 2, N
s        e
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        while n > 0:
            end = end.next
            n -= 1
        sentinal = ListNode(0)
        sentinal.next = head

        start = sentinal
        while end:
            start = start.next
            end = end.next
        
        start.next = start.next.next
        return sentinal.next


        
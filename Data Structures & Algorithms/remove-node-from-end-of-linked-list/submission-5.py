# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode()
        res.next = head
        back  = res
        front = res.next
        """
        s 1 2 3 4
          b     f
        s 1 2 N
        b     f

        """
        while n:
            front = front.next
            n -= 1
        
        while front:
            front = front.next
            back = back.next
        
        back.next = back.next.next
        return res.next
        

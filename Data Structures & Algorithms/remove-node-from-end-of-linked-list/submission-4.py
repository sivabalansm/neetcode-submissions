# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode()
        res.next = head
        l = res
        r = head

        for _ in range(n - 1):
            r = r.next

        while r.next:
            r = r.next
            l = l.next
        l.next = l.next.next
        return res.next
        

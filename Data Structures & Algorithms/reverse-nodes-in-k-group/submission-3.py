# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        def rev(node1, node2, left):
            prev = None
            if node2:
                prev = node2.next

            curr = node1
            stop = None
            if node2:
                stop = node2.next
            while curr != stop:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            left.next = prev
            return prev
        
        
            
        left = dummy
        curr = head
        while curr:
            start = curr
            end = curr
            for _ in range(k - 1):
                end = end.next
                if not end:
                    return dummy.next
            rev(start, end, left)
            left = start
            curr = start.next
        return dummy.next
            

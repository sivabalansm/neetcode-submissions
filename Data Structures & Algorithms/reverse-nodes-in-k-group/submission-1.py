# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode()
        res.next = head

        curr = head

        size = 0
        while curr:
            curr = curr.next
            size += 1
        
        def reverse_list(start, end, prev = None):
            prev = prev
            curr = start
            while curr != end:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp


        curr = head
        pre_start = res
        for _ in range(size // k):
            start = curr
            for _ in range(k - 1):
                curr = curr.next
            end = curr.next
            reverse_list(start, end, end)
            pre_start.next = curr
            pre_start = start
            curr = end
        return res.next

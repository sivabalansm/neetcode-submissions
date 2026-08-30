# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        l = head
        r = head
        pre_l = None
        for i in range(right - left):
            r = r.next
        for i in range(left - 1):
            pre_l = l
            l = l.next
            r = r.next
        
        r_next = r.next
        prev = r_next
        curr = l
        while curr != r_next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        if pre_l:
            pre_l.next = prev
        else:
            return prev
        
        return head




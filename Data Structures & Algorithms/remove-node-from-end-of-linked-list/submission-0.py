# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = 0
        curr = head
        while curr:
            k += 1
            curr =curr.next
        
        ff = k - n 


        curr = head
        prev = None
        for i in range(ff):
            prev = curr
            curr = curr.next

        if not prev and curr:
            return curr.next
        prev.next = curr.next
        return head
        


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        l = 0
        while cur:
            cur = cur.next
            l += 1
        if l == n:
            return None
        t = l - n
        cur = head
        prev = None
        for i in range(t):
            prev = cur
            cur = cur.next
        
        #print(prev.val)
        if prev.next:
            prev.next = prev.next.next
        else:
            prev.next = None
        return head

        

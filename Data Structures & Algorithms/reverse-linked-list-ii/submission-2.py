# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def rev(curr):
            tail = curr
            prev = None
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                if prev.val == right:
                    tail.next = curr
                    break
            head = prev
            return (head, tail)
            
        curr = head
        prev = None
        while curr:
            if curr.val == left:
                start, end = rev(curr)
                end.next = curr.next
                if prev:
                    prev.next = start
                    return head
                else:
                    return start
            prev = curr
            curr = curr.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            next_curr = curr.next
            n1 = curr.val
            n2 = curr.next.val
            gcd = math.gcd(n1, n2)
            gn = ListNode(gcd)
            curr.next = gn
            gn.next = next_curr
            curr = next_curr
        return head
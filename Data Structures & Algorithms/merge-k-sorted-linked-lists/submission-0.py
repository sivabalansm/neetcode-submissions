# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeList(head1, head2):
            head = ListNode()
            curr = head
            while head1 and head2:
                if head1.val < head2.val:
                    curr.next = head1
                    head1 = head1.next
                else:
                    curr.next = head2
                    head2 = head2.next
                curr = curr.next
            if head1:
                curr.next = head1
            elif head2:
                curr.next = head2
            return head.next
        
        head = None
        for ln in lists:
            head = mergeList(head, ln)
        return head


        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        ahead = curr = dummy     
        for _ in range(n):
            ahead = ahead.next
        while ahead and ahead.next:
            curr = curr.next
            ahead = ahead.next
        curr.next = curr.next.next
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(next=head)
        cur = head
        if not cur: return cur
        while cur.next:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = sentinel.next 
            sentinel.next = tmp

        return sentinel.next
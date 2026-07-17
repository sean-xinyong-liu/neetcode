# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(next=head)
        cur = head
        while cur and cur.next:
            next_node = cur.next
            cur.next = next_node.next
            next_node.next = sentinel.next 
            sentinel.next = next_node

        return sentinel.next
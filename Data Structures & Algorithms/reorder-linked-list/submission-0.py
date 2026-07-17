# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        first = head
        second = slow.next
        slow.next = None

        pre, cur = None, second
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        rev = pre
        while rev:
            nxt1 = first.next
            nxt2 = rev.next
            first.next = rev
            rev.next = nxt1
            rev = nxt2
            first = nxt1
        return 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        first = head
        second = slow.next
        slow.next = None

        prev, curr = None, second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second = prev
        while second:
            nxt1 = first.next
            nxt2 = second.next
            first.next = second
            second.next = nxt1
            second = nxt2
            first = nxt1
        return 


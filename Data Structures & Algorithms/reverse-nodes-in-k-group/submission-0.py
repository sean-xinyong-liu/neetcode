# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_kth(node, k):
            while node and k > 0:
                node = node.next
                k -= 1
            return node
        dummy = ListNode(next=head)
        group_prev = dummy
        while True:
            kth = get_kth(group_prev, k)
            if not kth:
                break
            group_next = kth.next
            group_start = group_prev.next

            prev = group_next
            curr = group_start
            while curr is not group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            group_prev.next = kth
            group_prev = group_start
        return dummy.next
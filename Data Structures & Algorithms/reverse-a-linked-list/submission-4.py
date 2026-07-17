class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = rev
            rev = cur
            cur = tmp
        return rev


    
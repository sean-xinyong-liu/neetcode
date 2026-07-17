# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = l3 = ListNode(0, None)     
        carry = 0
        while l1 or l2 or carry:
            if not l2:
                if carry:
                    l2 = ListNode(1, None)
                    carry = 0
                else:
                    l3.next = l1    
                    break
            if not l1:
                if carry:
                    l1 = ListNode(1, None)
                    carry = 0
                else:
                    l3.next = l2    
                    break

            val = l1.val + l2.val + carry
            if val >= 10:
                val = val - 10
                carry = 1
            else:
                carry = 0
            l3.next = ListNode(val, None)
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next
        return dummy.next
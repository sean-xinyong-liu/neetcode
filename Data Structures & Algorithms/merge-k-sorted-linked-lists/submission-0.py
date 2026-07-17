# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappop, heappush
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        tail = dummy
        for i, node in enumerate(lists):
            heappush(heap, (node.val, i, node))
        while heap:
            val, i, node = heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
        return dummy.next
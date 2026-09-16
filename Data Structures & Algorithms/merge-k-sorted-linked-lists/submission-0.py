import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min heap stores tuples: (value, list_index, node)
        min_heap = []
        
        # Step 1: Initialize heap with first node from each list
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(min_heap, (lst.val, i, lst))
        
        # Create dummy node to simplify result construction
        dummy = ListNode(0)
        current = dummy
        
        # Step 2: Process until heap is empty
        while min_heap:
            # Pop node with minimum value
            val, idx, node = heapq.heappop(min_heap)
            
            # Add to result
            current.next = node
            current = current.next
            
            # Push next node from same list if it exists
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))
        
        return dummy.next
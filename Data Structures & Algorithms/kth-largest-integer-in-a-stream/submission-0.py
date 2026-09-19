import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        # Add each number from the initial stream
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # If the heap hasn't reached size k yet, simply push the value
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        # If the new value is larger than the k-th largest (the root), 
        # push it into the heap and pop the smallest element to maintain size k
        elif val > self.min_heap[0]:
            heapq.heappushpop(self.min_heap, val)
        
        # The root of the min-heap is always the k-th largest element
        return self.min_heap[0]
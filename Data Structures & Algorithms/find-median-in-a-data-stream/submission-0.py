import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # max heap (stores negative values for smaller half)
        self.large = []  # min heap (stores larger half)

    def addNum(self, num: int) -> None:
        # Add to max heap first
        heapq.heappush(self.small, -num)
        
        # Ensure every element in small <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Maintain size constraint: small can have at most 1 more element
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # If odd number of elements, return top of small heap
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        # If even, return average of both heaps' tops
        return (-self.small[0] + self.large[0]) / 2.0
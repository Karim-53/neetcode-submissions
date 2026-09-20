import heapq
from collections import Counter
from typing import List
import math

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequency of each unique element: O(N)
        counts = Counter(nums)
        n_unique = len(counts)

        # Threshold decision: Method 1 is better when k is small relative to unique elements,
        # while Method 2 is faster when k approaches the number of unique elements.
        # Exact complexity comparison:
        # Method 1: U * log2(k)
        # Method 2: U + k * log2(U)
        cost_method1 = n_unique * math.log2(k)
        cost_method2 = n_unique + (k * math.log2(n_unique))

        if cost_method1 < cost_method2:
            return self._method1_min_heap(counts, k)
        else:
            return self._method2_max_heapify(counts, k)

    def _method1_min_heap(
        self, counts: Counter[int, int], k: int
    ) -> List[int]:
        """Method 1: Maintain a min-heap of maximum size k.

        Time: O(N + U log k) where U is number of unique elements. Space: O(U +
        k)
        """
        min_heap = []

        for num, freq in counts.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for freq, num in min_heap]

    def _method2_max_heapify(
        self, counts: Counter[int, int], k: int
    ) -> List[int]:
        """Method 2: Heapify the whole frequency array into a max-heap, then pop

        k elements. Time: O(N + U + k log U) where U is number of unique
        elements. Space: O(U)
        """
        # Python's heapq is a min-heap, so store negative frequencies for max-heap behavior
        max_heap = [(-freq, num) for num, freq in counts.items()]
        heapq.heapify(max_heap)  # O(U) time

        result = []
        for _ in range(k):
            freq, num = heapq.heappop(max_heap)  # O(log U) per pop
            result.append(num)

        return result
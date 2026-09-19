from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # Stores indices, with elements in decreasing order of their values
        res = []
        
        for i, val in enumerate(nums):
            # 1. Remove elements that are out of the current sliding window from the left
            if q and q[0] <= i - k:
                q.popleft()
                
            # 2. Maintain monotonicity: remove elements from the right that are smaller than the current element
            while q and nums[q[-1]] <= val:
                q.pop()
                
            # 3. Add current index
            q.append(i)
            
            # 4. The front of the deque is always the maximum for the window starting at i - k + 1
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res
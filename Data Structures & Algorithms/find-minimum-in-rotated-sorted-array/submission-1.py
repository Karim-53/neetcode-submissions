class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            # Condition: nums[mid] < nums[0]
            # Pattern: False, False, False... → True, True, True
            if nums[mid] < nums[0]:
                # mid is in rotated part, move right boundary
                right = mid
            else:
                # mid is in original sorted part, move left boundary
                left = mid + 1
        
        # Edge case: all False (no rotation) → minimum is nums[0]
        # Otherwise: minimum is at nums[left]
        return min(nums[0], nums[left])
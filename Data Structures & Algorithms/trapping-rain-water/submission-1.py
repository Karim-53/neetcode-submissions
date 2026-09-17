from typing import List

class Solution:
    """
    FIXED VERSION: Two-pass approach (left-to-right + right-to-left)

    Problem with single pass:
    [10, 1, 0, 1] - The [1, 0, 1] gets skipped because 1 < 10
    This case needs a RIGHT-TO-LEFT pass to catch water trapped by a SMALLER right boundary
    """

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        result = 0
        processed = [False] * n  # Track which positions we've already counted

        # ========== PASS 1: LEFT-TO-RIGHT ==========
        # Handles cases where right_peak >= left_peak
        prefix_sum = [0] * n
        prefix_sum[0] = height[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + height[i]

        left = 0
        while left < n and height[left] == 0:
            left += 1

        if left == n:
            return 0

        right = left + 1

        while right < n:
            if height[right] < height[left]:
                right += 1
            else:  # height[right] >= height[left]
                # Calculate water trapped between left and right
                num_positions = right - left - 1
                sum_between = prefix_sum[right - 1] - prefix_sum[left]
                water_trapped = num_positions * height[left] - sum_between
                result += water_trapped

                # Mark as processed
                for i in range(left, right + 1):
                    processed[i] = True

                left = right
                right += 1

        # ========== PASS 2: RIGHT-TO-LEFT ==========
        # Handles cases where left_peak > right_peak (CRITICAL CASE!)
        # Example: [10, 1, 0, 1] - the small valley on the right side

        suffix_sum = [0] * n
        suffix_sum[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + height[i]

        right = n - 1
        while right >= 0 and height[right] == 0:
            right -= 1

        if right < 0:
            return result

        left = right - 1

        while left >= 0:
            if height[left] < height[right]:
                left -= 1
            else:  # height[left] >= height[right]
                # Calculate water trapped between right and left
                num_positions = right - left - 1
                sum_between = suffix_sum[left + 1] - suffix_sum[right]
                water_trapped = num_positions * height[right] - sum_between

                # Only add if not already processed
                for i in range(left + 1, right):
                    if not processed[i]:
                        water_trapped -= height[i]  # Already subtracted in suffix calc

                # Actually, let me recalculate to avoid double counting...
                # Better approach: only count unprocessed positions
                for i in range(left + 1, right):
                    if not processed[i]:
                        water_at_i = height[right] - height[i]
                        if water_at_i > 0:
                            result += water_at_i
                        processed[i] = True

                right = left
                left -= 1

        return result

class Solution:

  def subarraySum(self, nums: List[int], k: int) -> int:
    count = 0
    current_sum = 0
    # Dictionary to store the frequency of prefix sums
    # {0: 1} handles the edge case where a subarray starts right from index 0
    prefix_counts = {0: 1}

    for num in nums:
      current_sum += num

      # Check if there is a previous prefix sum such that current_sum - prev_sum = k
      # Which rearranges to: prev_sum = current_sum - k
      diff = current_sum - k
      if diff in prefix_counts:
        count += prefix_counts[diff]

      # Add the current_sum to the map (or increment its frequency)
      prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

    return count
class Solution:
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     seen = set()
    #     for num in nums:
    #         if num in seen:
    #             return True
    #         seen.add(num)
    #     return False
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
# class Solution:
#     def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
# sort nums
# min = nums[0]

# cache
# def dp(remain, i: index in nums)
# if remain = 0 return solution and cache
# if remain smaller than min return No solution
# dp(remain, i+1) and or  dp(remain-nums[i], i) 



from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        
        def backtrack(remain: int, start: int, path: List[int]):
            if remain == 0:
                res.append(list(path))
                return
            
            for i in range(start, len(nums)):
                if nums[i] > remain:
                    break # Pruning: since nums is sorted, further elements are too large
                path.append(nums[i])
                backtrack(remain - nums[i], i, path) # i is reused because numbers can be chosen unlimited times
                path.pop()
                
        backtrack(target, 0, [])
        return res
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        bitmap = [False]*(n+5)
        for e in nums:
            if e<0 or e>n : continue
            bitmap[e] = True

        bitmap[0] = True
        for i,e in enumerate(bitmap):
            if not e:
                return i

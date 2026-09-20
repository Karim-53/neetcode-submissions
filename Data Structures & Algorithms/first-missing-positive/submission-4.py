class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        _min = 1
        _max = len(nums)+1
        i=0
        while i <len(nums):
            e = nums[i]
            if e is None:
                i+=1
                continue

            if e>=_max or e<_min: # negative , too high or duplicate
                nums[i] = None
                _max -= 1
                if _min==_max : return _min
                i+=1
            else:
                if e ==_min:
                    _min+=1
                    if _min==_max : return _min

                if i==e-1: # in place nothing to do
                    i+=1
                else:
                    # swap
                    other = nums[e-1]
                    nums[e-1] = e
                    if other == e:
                        nums[i] = None
                    else:
                        nums[i] = other

        for i in range(_min-1,      min(_max+1,len(nums))      ):
            if nums[i] is None:
                return i+1
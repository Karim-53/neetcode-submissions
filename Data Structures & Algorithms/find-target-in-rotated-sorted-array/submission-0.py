# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
# compare the first and last eleemnt to see if the array is rotated or not 
# if not rotated a[0] < a[-1] then do a classical binary search for the element 
# if rotated because a[0] > a[-1] then first do a binary to find the cliff:
#    a[i] > a[0] is true for the first part of the array and false in the second half 
# once the cliff detected you know the 2 segments [a[0],max] [min, a[-1]] decide to bisect in one of them or return -1 already

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Fix: Use <= to handle arrays of length 1 or unrotated arrays properly
        if nums[0] <= nums[-1]:
            # Classical binary search for unrotated array
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        # If rotated, find the cliff (pivot) where nums[i] >= nums[0]
        left, right = 0, len(nums) - 1
        pivot = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= nums[0]:
                pivot = mid
                left = mid + 1
            else:
                right = mid - 1
                
        # Decide which of the two segments to search in
        if target >= nums[0]:
            left, right = 0, pivot
        else:
            left, right = pivot + 1, len(nums) - 1
            
        # Binary search in the selected segment
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1
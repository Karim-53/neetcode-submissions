class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def _bisect(left= 0, right=len(nums) - 1, cliff_here=True):
        
            if not (left <= right):return False
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True
            # Check if the left half is normally sorted
            if nums[left] < nums[mid]:
                # Check if target lies within the sorted left half
                if nums[left] <= target < nums[mid]:
                    return _bisect(left=left, right = mid - 1, cliff_here=False)  # Go left
                else:
                    return _bisect(left = mid + 1,right=right, cliff_here=cliff_here)   # Go right
            # Otherwise, the right half must be normally sorted
            elif nums[mid] < nums[right]: # Check if the left half is normally sorted
                # Check if target lies within the sorted right half
                if nums[mid] < target <= nums[right]:
                        return _bisect(left = mid + 1,right=right, cliff_here=False)   # Go right
                else:
                        return _bisect(left,right = mid - 1, cliff_here=cliff_here)  # Go left
            else: # left >= mid >= right 
                # this mean left = mid = right
                if not cliff_here:
                    return False
                if _bisect(left,right = mid - 1, cliff_here=cliff_here):  # Go left
                    return True
                if _bisect(left = mid + 1,right=right, cliff_here=cliff_here):   # Go right
                    return True
                return False

        return _bisect()
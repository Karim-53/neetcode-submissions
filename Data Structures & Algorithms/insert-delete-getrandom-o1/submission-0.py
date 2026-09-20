import random

class RandomizedSet:
    def __init__(self):
        """Bismillah: Initializing our dynamic list and hash map."""
        self.nums = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        
        # Swap the element to be deleted with the last element in the list
        last_element = self.nums[-1]
        idx_to_remove = self.val_to_index[val]
        
        self.nums[idx_to_remove] = last_element
        self.val_to_index[last_element] = idx_to_remove
        
        # Remove the last element and delete from the dictionary
        self.nums.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
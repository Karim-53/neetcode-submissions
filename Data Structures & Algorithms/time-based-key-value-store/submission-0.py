from bisect import bisect_right

class TimeMap:

    def __init__(self):
        # Maps key -> (timestamps_list, values_list)
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = ([], [])
        
        self.store[key][0].append(timestamp)
        self.store[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        timestamps, values = self.store[key]
        
        # Find the rightmost insertion point to get the largest timestamp <= target
        idx = bisect_right(timestamps, timestamp)
        
        if idx == 0:
            return ""
        
        return values[idx - 1]
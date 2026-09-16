class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Index the characters of t in a dictionary
        dict_t = {}
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1
        
        # Number of unique characters in t that must be present in window
        required = len(dict_t)
        
        # Dictionary counting characters in current window
        window_counts = {}
        
        # formed: how many unique chars in window have the desired frequency
        formed = 0
        
        # Two pointers: a (left) <= b (right)
        a, b = 0, 0
        
        # Best window: (length, left_index, right_index)
        best = float("inf"), None, None
        
        while b < len(s):
            # Expand window: move pointer b to the right
            char = s[b]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Check if this character's count now matches t's requirement
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            
            # Contract window: move pointer a to the left
            # while the window is valid (contains all chars from t)
            while a <= b and formed == required:
                char = s[a]
                
                # Save this window if it's better than best
                if b - a + 1 < best[0]:
                    best = (b - a + 1, a, b)
                
                # Remove character at pointer a from window
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                
                # Move pointer a right (shrink window from left)
                a += 1
            
            # Move pointer b to expand window
            b += 1
        
        # Return the best substring found
        return "" if best[0] == float("inf") else s[best[1]:best[2] + 1]
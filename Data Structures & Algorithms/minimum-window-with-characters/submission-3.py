class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""
        
        # Use arrays instead of dictionaries (faster for ASCII)
        dict_t = [0] * 128  # ASCII character set
        window_counts = [0] * 128
                
        # Count characters in t
        for char in t:
            dict_t[ord(char)] += 1
        # # Count characters in s
        # dict_s = [0] * 128  # ASCII character set
        # for char in s:
        #     dict_s[ord(char)] += 1
        # # quick check if there is a valid solution
        # for c in range(len(dict_s)):
        #     if dict_t[c] > dict_s[c]:
        #         return ""
        
        # Number of unique characters in t with non-zero count
        required = sum(1 for count in dict_t if count > 0)
        formed = 0
        
        a, b = 0, 0
        best = float("inf"), None, None
        
        while b < len(s):
            # Expand window: move pointer b
            char_b = s[b]
            window_counts[ord(char_b)] += 1
            
            # Check if this character now matches required count
            if window_counts[ord(char_b)] == dict_t[ord(char_b)]:
                formed += 1
            
            # Contract window: move pointer a
            while a <= b and formed == required:
                char_a = s[a]
                
                # Save best window
                if b - a + 1 < best[0]:
                    best = (b - a + 1, a, b)
                
                # Remove character at a
                window_counts[ord(char_a)] -= 1
                if window_counts[ord(char_a)] < dict_t[ord(char_a)]:
                    formed -= 1
                
                a += 1
            
            b += 1
        
        return "" if best[0] == float("inf") else s[best[1]:best[2] + 1]
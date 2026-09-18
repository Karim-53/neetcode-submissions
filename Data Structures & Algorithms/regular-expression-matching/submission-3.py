class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def dp(i, j):  # i = index in s, j = index in p
            # Check cache
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base case: reached end of pattern
            if j == len(p):
                return i == len(s)
            
            # Check if first character matches
            first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            if j + 1 < len(p) and p[j + 1] == '*':
                # Pattern has char*
                # Option 1: Skip char* (progress on p)
                # Option 2: Match current char and stay at p (progress on s)
                if dp(i, j + 2) or (first_match and dp(i + 1, j)):
                    return True
            else:
                # No star, must match both characters
                if first_match and dp(i + 1, j + 1):
                    return True
            
            # Only memoize False
            memo[(i, j)] = False
            return False
        
        return dp(0, 0)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Precompute lower_bound[j] = minimum characters needed to match p[j:]
        # Treating char* as 0 (can skip it)
        lower_bound = [0] * (len(p) + 1)
        for j in range(len(p) - 1, -1, -1):
            if j + 1 < len(p) and p[j + 1] == '*':
                # char* can match 0 characters, so just need what comes after
                lower_bound[j] = lower_bound[j + 2]
            else:
                # Single character must match 1 character from s
                lower_bound[j] = 1 + lower_bound[j + 1]
        
        memo = set()  # Track (i, j) pairs that return False
        
        def dp(i, j):
            # Early pruning: not enough characters left to satisfy pattern
            if len(s) - i < lower_bound[j]:
                return False
            
            # Memoization: if already computed as False, return False
            if (i, j) in memo:
                return False
            
            # Base case: reached end of pattern
            if j == len(p):
                return i == len(s)
            
            # Check if current character matches
            first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            if j + 1 < len(p) and p[j + 1] == '*':
                # char* pattern: try skip (j+2) or match (j stays same)
                if dp(i, j + 2) or (first_match and dp(i + 1, j)):
                    return True
            else:
                # No star: must match current characters
                if first_match and dp(i + 1, j + 1):
                    return True
            
            memo.add((i, j))
            return False
        
        return dp(0, 0)
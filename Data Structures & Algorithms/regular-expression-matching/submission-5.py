class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        failed = set()

        def backtrack(i: int, j: int) -> bool:
            if j < 0:
                return i < 0
            if (i, j) in failed:
                return False
            if p[j] == "*":
                ok = backtrack(i, j - 2) or (
                    i >= 0 and (p[j - 1] == s[i] or p[j - 1] == ".") and backtrack(i - 1, j))
            else:
                ok = i >= 0 and (p[j] == s[i] or p[j] == ".") and backtrack(i - 1, j - 1)
            if not ok:
                failed.add((i, j))
            return ok

        return backtrack(len(s) - 1, len(p) - 1)
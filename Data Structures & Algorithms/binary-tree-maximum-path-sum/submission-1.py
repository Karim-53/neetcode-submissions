# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = float('-inf')
        
        def dfs(node):
            if not node:
                return 0  # Clean: null nodes contribute 0
            
            # Get max path sum from children (0 if negative)
            left_sum = max(0, dfs(node.left))
            right_sum = max(0, dfs(node.right))
            
            # Best path pivoting at this node
            self.result = max(self.result, node.val + left_sum + right_sum)
            
            # Return single path down to parent
            return node.val + max(left_sum, right_sum)
        
        dfs(root)
        return self.result
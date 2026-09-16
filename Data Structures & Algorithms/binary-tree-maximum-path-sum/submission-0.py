# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.current_best = float('-inf')
        
        def dfs(node):
            # Base case: null node
            if node is None:
                return float('-inf')
            
            # Recursively get best sums from left and right children
            best_left_child = dfs(node.left)
            best_right_child = dfs(node.right)
            
            # Best sum going left: current node + best from left subtree
            # (if left is negative, we can ignore it by using 0)
            best_left = node.val + max(0, best_left_child)
            
            # Best sum going right: current node + best from right subtree
            best_right = node.val + max(0, best_right_child)
            
            # Update current_best: consider all paths that can pivot at this node
            # - best_left: path ending at this node going left
            # - best_right: path ending at this node going right
            # - best_left + best_right - node.val: path through this node (subtract node.val to avoid double counting)
            self.current_best = max(
                self.current_best,
                best_left,
                best_right,
                best_left + best_right - node.val
            )
            
            # Return to parent: max of left or right (only one branch can be passed up)
            return max(best_left, best_right)
        
        dfs(root)
        return self.current_best
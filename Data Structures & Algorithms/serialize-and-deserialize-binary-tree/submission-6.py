import json
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        """DFS that returns a list of (val, left_idx, right_idx) tuples, then joins with ';'"""
        result = []
        
        def dfs(node):
            if node is None:
                return None
            
            # Reserve space for this node (append placeholder)
            current_idx = len(result)
            result.append(None)
            
            # Recurse and collect indices
            left_idx = dfs(node.left) if node.left else None
            right_idx = dfs(node.right) if node.right else None
            
            result[current_idx] = [node.val, left_idx, right_idx]  # List, not tuple
            return current_idx
    
        dfs(root)
        return json.dumps(result)  # Much faster than string repr + join



    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Reconstruct tree from serialized string"""
        if not data or data == "":
            return None
        
        nodes = json.loads(data)  # Single fast parse, not eval()
        
        # Reconstruct tree using indices
        def build(idx):
            if idx is None:
                return None
            
            val, left_idx, right_idx = nodes[idx]
            node = TreeNode(val)
            node.left = build(left_idx)
            node.right = build(right_idx)
            return node
        
        return build(0) if nodes else None


# # Test with your example
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(5)

# encoded = serialize(root)
# print(f"Encoded: {encoded}")
# # Output: (1, 1, 2);(2, None, None);(3, 3, 4);(4, None, None);(5, None, None)

# decoded = deserialize(encoded)
# print(f"Decoded root: {decoded.val}, left: {decoded.left.val}, right: {decoded.right.val}")
# # Output: Decoded root: 1, left: 2, right: 3
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.count = 1  # Handles duplicate elements gracefully in the window

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self._height(y.left), self._height(y.right)) + 1
        x.height = max(self._height(x.left), self._height(x.right)) + 1
        return x

    def _left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self._height(x.left), self._height(x.right)) + 1
        y.height = max(self._height(y.left), self._height(y.right)) + 1
        return y

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return Node(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        else:
            node.count += 1
            return node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        balance = self._get_balance(node)

        # Left Left
        if balance > 1 and val < node.left.val:
            return self._right_rotate(node)
        # Right Right
        if balance < -1 and val > node.right.val:
            return self._left_rotate(node)
        # Left Right
        if balance > 1 and val > node.left.val:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        # Right Left
        if balance < -1 and val < node.right.val:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if node.count > 1:
                node.count -= 1
                return node
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Node with two children: Get the inorder successor
            temp = self._get_min(node.right)
            node.val = temp.val
            node.count = temp.count
            temp.count = 1  # Reset count for deletion of successor node
            node.right = self._delete_min(node.right)

        if not node:
            return None

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        balance = self._get_balance(node)

        # Rebalancing rotations during deletion
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _get_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def _delete_min(self, node):
        if not node.left:
            return node.right
        node.left = self._delete_min(node.left)
        return node

    def get_max(self):
        current = self.root
        while current.right:
            current = current.right
        return current.val

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        bst = AVLTree()
        res = []
        
        for i in range(k):
            bst.insert(nums[i])
            
        res.append(bst.get_max())
        
        for i in range(k, len(nums)):
            bst.delete(nums[i - k])
            bst.insert(nums[i])
            res.append(bst.get_max())
            
        return res
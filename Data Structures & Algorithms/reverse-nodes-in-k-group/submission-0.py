# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverse the first k nodes, then the next k nodes, and so on.
        Uses a stack to handle the reversal of each group.
        """
        
        # Definition for singly-linked list node
        # class ListNode:
        #     def __init__(self, val=0, next=None):
        #         self.val = val
        #         self.next = next
        
        def has_k_nodes(node):
            """Check if there are at least k nodes starting from node"""
            count = 0
            while node and count < k:
                count += 1
                node = node.next
            return count == k
        
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        
        # Process groups of k nodes
        while has_k_nodes(prev_group.next):
            stack = []
            current = prev_group.next
            
            # Push k nodes onto the stack
            for _ in range(k):
                stack.append(current)
                current = current.next
            
            # Pop from stack and reconnect (reverses the order)
            while stack:
                node = stack.pop()
                prev_group.next = node
                prev_group = node
            
            # Connect to the next group
            prev_group.next = current
        
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverse groups of k nodes. If fewer than k nodes remain, leave them as is.
        """
        
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        
        while True:
            stack = []
            current = prev_group.next
            
            # Try to push k nodes onto the stack
            for _ in range(k):
                if not current:
                    # Reached end of list before filling k nodes
                    return dummy.next
                stack.append(current)
                current = current.next
            
            # We have k nodes, pop them to reverse
            while stack:
                node = stack.pop()
                prev_group.next = node
                prev_group = node
            
            # Connect to next group
            prev_group.next = current
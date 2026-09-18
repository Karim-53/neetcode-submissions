# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Reverse each group of k nodes using a segment-based approach."""
        result = ListNode(0)  # Dummy node to build result
        result_tail = result

        current = head

        while current:
            segment_start = current  # Memo: remember where this segment starts
            segment_count = 0

            # Try to collect k nodes
            while current and segment_count < k:
                current = current.next
                segment_count += 1

            # Check if we got a full segment of k nodes
            if segment_count < k:
                # Incomplete segment: append remaining nodes as-is
                result_tail.next = segment_start
                return result.next

            # We have k nodes, reverse them
            prev = None
            node = segment_start
            for _ in range(k):
                next_temp = node.next
                node.next = prev
                prev = node
                node = next_temp

            # prev now points to the head of the reversed segment
            # segment_start is now the tail of the reversed segment
            result_tail.next = prev
            result_tail = segment_start

        return result.next

class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Maps key to its corresponding Node in the linked list
        
        # Initialize dummy head and tail nodes to avoid edge cases during insertions/deletions
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Removes a node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_tail(self, node: Node):
        """Adds a node right before the tail (marking it as most recently used)."""
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # Move the accessed node to the tail (most recently used position)
        self._remove(node)
        self._add_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            # Update position to most recently used
            self._remove(node)
            self._add_to_tail(node)
        else:
            if len(self.cache) >= self.capacity:
                # Evict the least recently used item (the one right after the dummy head)
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]
            
            # Insert the new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_tail(new_node)
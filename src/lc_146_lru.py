class Node:
    """Doubly linked list node storing a cache key-value pair."""

    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """Doubly linked list with sentinel head/tail for O(1) add/remove."""

    def __init__(self) -> None:
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.tail.prev = self.head
        self.head.next = self.tail

    def delete(self, node: Node) -> None:
        prev = node.prev
        next_node = node.next
        prev.next = next_node
        next_node.prev = prev
        # Break references to avoid cycles
        node.next = None
        node.prev = None

    def append(self, node: Node) -> None:
        prev_tail = self.tail.prev
        prev_tail.next = node
        node.prev = prev_tail
        node.next = self.tail
        self.tail.prev = node

    def move_to_last(self, node: Node) -> None:
        if node == self.tail.prev:
            # Already last
            return
        self.delete(node)
        self.append(node)


class LRUCache:
    """LRU cache with O(1) get and put using a hash map + doubly linked list."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, Node] = {}
        self.dlist = DoublyLinkedList()

    def get(self, key: int) -> int:
        """Return value if key exists, else -1. Moves key to most recently used."""
        if key not in self.cache:
            return -1

        res = self.cache[key]
        self.dlist.move_to_last(res)
        return res.value

    def put(self, key: int, value: int) -> None:
        """Insert or update key-value. Evicts LRU item if at capacity."""
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.dlist.move_to_last(node)
            return

        if self.capacity == len(self.cache):
            # evict
            head = self.dlist.head.next
            self.dlist.delete(head)
            del self.cache[head.key]

        new_node = Node(key, value)
        self.dlist.append(new_node)
        self.cache[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

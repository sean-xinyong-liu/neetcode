class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_first(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next = node
        node.next.prev = node

    def _move_to_first(self, node):
        self._remove(node)
        self._add_first(node)

    def _remove_last(self):
        node = self.tail.prev
        self._remove(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_first(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_first(node)
            return

        node = Node(key, value)
        self.cache[key] = node
        self._add_first(node)

        if len(self.cache) > self.capacity:
            removed = self._remove_last()
            del self.cache[removed.key]
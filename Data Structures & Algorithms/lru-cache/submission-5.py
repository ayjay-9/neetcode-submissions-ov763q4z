class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        self.map.move_to_end(key)
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        # 1. Update the key's value if it exists
        # 2. Add new key-value
        # 3. Remove the last used key
        # put() can only do either of the three

        if key in self.map:
            self.map[key] = value
            self.map.move_to_end(key)
            return

        if len(self.map) == self.capacity:
            self.map.popitem(last=False)

        self.map[key] = value

# 체이닝 방식

class HashNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def _hash_function(self, key):
        return key % self.size

    def put(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = HashNode(key, value)
        else:
            node = self.table[index]
            while node.next is not None:
                node = node.next
            node.next = HashNode(key, value)

    def get(self, key):
        index = self._hash_function(key)
        node = self.table[index]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key):
        index = self._hash_function(key)
        node = self.table[index]
        prev_node = None
        while node is not None:
            if node.key == key:
                if prev_node is None:
                    self.table[index] = node.next
                else:
                    prev_node.next = node.next
                return
            prev_node = node
            node = node.next

ht = HashTable()

ht.put(1, 1)
ht.put(2, 2)
assert ht.get(1) == 1
assert ht.get(2) == 2
assert ht.get(3) == -1

ht.put(12, 1)
ht.put(22, 2)
ht.put(32, 3)
assert ht.get(12) == 1
assert ht.get(22) == 2
assert ht.get(32) == 3

ht.remove(12)
assert ht.get(2) == 2
assert ht.get(12) == -1
assert ht.get(22) == 2
assert ht.get(32) == 3

ht.get(2)
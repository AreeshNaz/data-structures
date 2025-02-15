class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
    def __repr__(self):
        return f"({self.key}: {self.value})"

class HashMap:
    def __init__(self):
        self.bucket_size = 10
        self.elements = [None] * self.bucket_size

    def hashFunction(self, key: int):
        return key % self.bucket_size

    def put(self, key: int, value: int):
        index = self.hashFunction(key)
        new_node = Node(key, value)
        if self.elements[index] is None:
            self.elements[index] = new_node
        else:
            current = self.elements[index]
            while current.next is not None:
                current = current.next
            current.next = new_node

    def get(self, key: int):
        index = self.hashFunction(key)
        current = self.elements[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def rem(self, key: int):
        index = self.hashFunction(key)
        current = self.elements[index]
        prev = None
        while current:
            if current.key == key:
                if prev is None:
                    self.elements[index] = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next

h = HashMap()
h.put(1, 100)
h.put(2, 200)
h.put(3, 300)
h.put(5, 500)
h.put(5, 600)
print([str(x) if x is None else str(x) for x in h.elements])

h.put(13, 1300)
h.rem(5)
print([str(x) if x is None else str(x) for x in h.elements])

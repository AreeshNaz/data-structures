class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        
    def __repr__(self):
        return f"({self.value})"

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value)

    def display(self):
        node = self.head
        while node:
            print(node.value, "->", end="", sep="")
            node = node.next
        print()

    def search(self, key):
        node = self.head
        while node:
            if node.value.key == key:
                return node.value
            node = node.next
        return None
    
    def remove(self, key):
        node = self.head
        prev = None
        while node:
            if node.value.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.head = node.next
                return True
            prev = node
            node = node.next
        return False
    
    def __repr__(self):
        _str = ""
        node = self.head
        while node:
            _str += f"{node.value}->"
            node = node.next
        return _str

class Bucket:
    def __init__(self, k, v):
        self.key = k
        self.value = v
    
    def __repr__(self) -> str:
        return f"{self.key}:{self.value}"

class MyHashMap:
    def __init__(self):
        self.hashSize = 676
        self.arr = [None] * self.hashSize

    def put(self, key: str, value: str):
        x = self.hash_fun(key)
        if self.arr[x] is None:
            self.arr[x] = LinkedList()
        self.arr[x].append(Bucket(key, value))

    def get(self, key: str):
        x = self.hash_fun(key)
        if self.arr[x] is not None:
            bucket = self.arr[x].search(key)
            return bucket.value if bucket else None
        return None

    def remove(self, key: str):
        x = self.hash_fun(key)
        if self.arr[x] is not None:
            removed = self.arr[x].remove(key)
            return removed
        return False

    def hash_fun(self, x):
        if isinstance(x, str):
            return (ord(x[0]) * 26 + ord(x[1])) % self.hashSize
        return -1

myHashMap = MyHashMap()

myHashMap.put("AAad", "0337 03332")
myHashMap.put("ABad", "0337 03332")
myHashMap.put("ADsab", "8332 03331")

print(myHashMap.get("ADsab"))
print(myHashMap.arr)

myHashMap.remove("ABad")
print(myHashMap.get("ABad"))
print(myHashMap.arr)

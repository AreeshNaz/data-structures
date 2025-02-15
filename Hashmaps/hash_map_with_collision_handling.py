class HashMap:
    def __init__(s):
        s.bucket_size = 10
        s.elements = [[] for _ in range(s.bucket_size)]

    def hashFunction(s, key: int):
        return key % s.bucket_size

    def put(s, key: int, value: int):
        index = s.hashFunction(key)
        for pair in s.elements[index]:
            if pair[0] == key:
                pair[1] = value
                return
        s.elements[index].append([key, value])

    def get(s, key: int):
        index = s.hashFunction(key)
        for pair in s.elements[index]:
            if pair[0] == key:
                return pair[1]
        return -1

    def rem(s, key: int):
        index = s.hashFunction(key)
        for i, pair in enumerate(s.elements[index]):
            if pair[0] == key:
                del s.elements[index][i]
                return

h = HashMap()
h.put(1, 100)
h.put(2, 200)
h.put(3, 500)
h.put(5, 200)
h.put(5, 700)
print(h.elements)
h.rem(5)
print(h.elements)

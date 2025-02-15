class HashTable(object):
    def __init__(self):
        # Table size
        self.table = [set() for _ in range(10000)]

    def store(self, string):
        """Store a string in the table."""
        hash_code = self.calculate_hash_value(string)
        self.table[hash_code].add(string)

    def lookup(self, string):
        """Return the hash value if the string exists in the table.
        Return -1 otherwise."""
        hash_code = self.calculate_hash_value(string)
        if string in self.table[hash_code]:
            return hash_code
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calculate a hash value from a string."""
        hash_code = (ord(string[0]) * 256 + ord(string[1])) % 10000
        return hash_code



hash_table = HashTable()

print(hash_table.calculate_hash_value('UDOMETER'))  # Should be 8568
print(hash_table.lookup('UDOMETER'))  # Should be -1
hash_table.store('UDOMETER')
print(hash_table.lookup('UDOMETER'))  # Should be 8568
hash_table.store('UDINE')
print(hash_table.lookup('UDINE'))  # Should be 8568

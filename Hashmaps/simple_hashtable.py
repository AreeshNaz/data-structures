class HashTable(object):
    def __init__(self):
        
        self.table = [None] * 10000

    def store(self, string):
        """Store a string in the table."""
        hash_code = self.calculate_hash_value(string)
        if self.table[hash_code] is None:
            self.table[hash_code] = [string]  
        else:
            self.table[hash_code].append(string)  

    def lookup(self, string):
        """Return the hash value if the string exists in the table.
        Return -1 otherwise."""
        hash_code = self.calculate_hash_value(string)
        if self.table[hash_code] is not None and string in self.table[hash_code]:
            return hash_code
        return -1

    def calculate_hash_value(self, string):
        """Calculate a hash value from the first two letters of a string."""
        hash_code = (ord(string[0]) * 100 + ord(string[1])) % 10000
        return hash_code



hash_table = HashTable()


print(hash_table.calculate_hash_value('UDOMETER'))  


print(hash_table.lookup('UDOMETER'))  

hash_table.store('UDOMETER')
print(hash_table.lookup('UDOMETER'))  
hash_table.store('UDINE')
print(hash_table.lookup('UDINE'))  

class HashTable(object):
    def __init__(self):
        self.table = [None]*10

    def store(self, value):
        """TODO: Input a number that's stored in 
        the table."""
        for i in range(10):
            hash_code = self.calculate_hash_value(i+value) 
            if self.table[hash_code] is None: 
                self.table[hash_code] = value
                return
       
        print("No space left: increase array size")
        
        
            
    def lookup(self, value):
        """TODO: Return the position where element is stored.
        otherwise Return -1 ."""
        for i in range(10):
            hash_code = self.calculate_hash_value(i+value) 
            if self.table[hash_code]: 
                if self.table[hash_code] == value: 
                    return hash_code
        return -1 

    def calculate_hash_value(self, value):  
        """TODO: Helper function to calulate a
        hash value from a string."""
        hash_code = value%10 
        return hash_code
    
    
hash_table = HashTable()


print (hash_table.calculate_hash_value(3))    
print (hash_table.calculate_hash_value(13))    
print (hash_table.calculate_hash_value(23))    


print (hash_table.lookup(23))                  


hash_table.store(3)
print (hash_table.lookup(3))                 


hash_table.store(13)
print (hash_table.lookup(13))                  


hash_table.store(23)
print (hash_table.lookup(23))
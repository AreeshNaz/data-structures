class Node:
    def __init__(self,v):
        self.value = v
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            node = self.head
            while node.next != None:
                node = node.next
            node.next = Node(value)

    def search(self, value):
        node = self.head
        count = 1            
        while node != None:            
            if node.value == value:
                return count
            node = node.next
            count += 1           
        return -1

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hash_code = self.calculate_hash_value(string)
        if self.table[hash_code]:
            self.table[hash_code].append(string)
        else:
            self.table[hash_code] = LinkedList()
            self.table[hash_code].append(string)
            
    def lookup(self, string):
        hash_code = self.calculate_hash_value(string)
        if self.table[hash_code]:
                return self.table[hash_code].search(string)
        return -1

    def calculate_hash_value(self, string):
        hash_code = ord(string[0])*100 + ord(string[1])
        return hash_code
    
hash_table = HashTable()

print (hash_table.calculate_hash_value('SAAD'))    
print (hash_table.lookup('SAAD'))                  
hash_table.store('SAAD')
print (hash_table.lookup('SAAD'))                  

print (hash_table.calculate_hash_value('SAMP'))    
hash_table.store('SAMP')                          
print (hash_table.lookup('SAMP'))                  

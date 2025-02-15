
class MyHashMap:

    def __init__(self):
        self.hashSize = 11
        self.arr = [None]*self.hashSize

    def put(self, key, value):
        x = self.hash_fun(key)
        self.arr[x] = value


    def get(self, key):
        x = self.hash_fun(key)
        return self.arr[x]

    def remove(self, key):
        x = self.hash_fun(key)
        self.arr[x] = None
    
    def hash_fun(self,x):
        return x



myHashMap = MyHashMap();
myHashMap.put(1, 1); 
myHashMap.put(2, 2); 
myHashMap.put(2, 6); 
myHashMap.remove(2)
myHashMap.put(10,5); # error 
myHashMap.put(0,90); 
print(myHashMap.arr)
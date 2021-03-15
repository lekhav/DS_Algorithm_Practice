class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

# Hashing + LL Linear Chaining
# Hashing + BST as bucket
# Double Hashing, O[1] Time, O[N] Space


class Hashset_DoubleHashing:
    def __init__(self):
        self.size = 1001
        self.hashSet = [None]*self.size
        
    def hashFunction1(self, key):
        return key % self.size
    def hashFunction2(self, key):
        return key // self.size

    def add(self, key):
        h1 = self.hashFunction1(key)
        h2 = self.hashFunction2(key)
        if self.hashSet[h1] == None:
            self.hashSet[h1] = [None]*self.size
        
        self.hashSet[h1][h2] = key
        

    def remove(self, key):
        h1 = self.hashFunction1(key)
        h2 = self.hashFunction2(key)
        if self.hashSet[h1] == None:
            return
        self.hashSet[h1][h2] = None

    def contains(self, key):
        h1 = self.hashFunction1(key)
        h2 = self.hashFunction2(key)
        if self.hashSet[h1] == None:
            return False
        
        if self.hashSet[h1][h2] != None:
            return True
        return False



# -----------------------------------------------------------
class Node:
    def __init__(self, key, val):
        self.key = key
        self.next = None

class hashSet_LLchaining:
    def __init__(self):
        self.size = 1000
        self.hashSet = [None]*self.size
        
    def hashFunction(self, key):
        return key % self.size

    def findNode(self, key):
        hashcode = self.hashFunction(key)
        node = self.hashSet[hashcode]
        previous = None
        
        while node != None and node.key != key:
            if node.key == key:
                return previous
            previous = node
            node = node.next
        return previous
    
    def add(self, key):
        hashcode = self.hashFunction(key)
        if self.hashSet[hashcode] == None:
            self.hashSet[hashcode] = Node(-1) 
        
        previous = self.findNode(key)
        if previous.next == None:
            previous.next = Node(key)
    

    def remove(self, key: int) -> None:
        hashcode = self.hashFunction(key)
        if self.hashSet[hashcode] == None:
            return 
        previous = self.findNode(key)
        if previous.next == None:
            return 
        previous.next = previous.next.next

    def contains(self, key: int) -> bool:
        hashcode = self.hashFunction(key)
        if self.hashSet[hashcode] == None:
            return False
        previous = self.findNode(key)
        if previous.next == None:
            return False
        elif previous.next.key == key:
            return True
        




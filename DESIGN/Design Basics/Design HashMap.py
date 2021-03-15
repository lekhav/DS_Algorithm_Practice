# Design Hashmap (https://leetcode.com/problems/design-hashmap/)

# Design a HashMap without using any built-in hash table libraries.
# To be specific, your design should include these functions: Follow up: How would you handle collisions in HashMap?
# put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
# get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.


# ————————————————————————————————————————————————————————————————————————————————————————————————
# Simple Remainder method, create hashvalue using the key,
# if slot is empty we create a linkedlist node and set the key value tuple

# Collision Resolution by Linear Chaining (LinkedList)
# hashvalue having a collision, use linked list for chaining
    #if the key matches, update the key value pair & return from there
    #if key value doesnt match & next pointer == None, we update the next pointer to a new node having the key, value tuple
    #if key value doesnt match & if linkedlist exists, then iterate through the next until next pointer is None and set the next pointer to a new node having the key, value tuple
            

# ————————————————————————————————————————————————————————————————————————————————————————————————
# Find the Index 
# Find the Node
# put function
# get function
# remove function


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
   
class HashMap_LLchaining:
    def __init__(self):
        self.size = 1000
        self.map = [None]*self.size

    def findIndex(self, key):
        return key % self.size

    def findNode(self, key):
        index = self.findIndex(key)
        node = self.map[index]
        previous = None
        while node != None and node.key != key:
            previous = node
            node = node.next
        return previous

    def put(self, key, val):
        index = self.findIndex(key)

        if self.map[index] == None:
            self.map[index] = Node(-1, -1)

        previous = self.findNode(key)        
        if previous.next == None:
            previous.next = Node(key, val)
        else:
            previous.next.val = val
            
    
    def get(self, key):
        index = self.findIndex(key)
        if self.map[index] == None:
            return -1
        
        previous = self.findNode(key)
        if previous.next == None:
            return -1
        return previous.next.val

    def remove(self, key):
        index = self.findIndex(key)
        if self.map[index] == None:
            return
    
        previous = self.findNode(key)
        if previous.next == None:
            return
        previous.next = previous.next.next

                    



                    
                

if __name__ == "__main__":
    obj = HashMap_LLchaining() 
    obj.put(1,1)
    obj.put(2,2)
    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(2))
    obj.put(2,1)
    print(obj.get(2))
    obj.remove(2)
    print(obj.get(2))


            



        


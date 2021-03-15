## Problem : LRU Cache(https://leetcode.com/problems/lru-cache/)

# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# The cache is initialized with a positive capacity.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4


# ————————————————————————————————————————————————————————————————————————————————————————————————
class DLLnode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.previous = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        
        # cache ===> { KEY : DLL (order of elements accessed, LRU at Tail) }
        # storing every Node to its Key in cache HashMap
        # Initiate a DLL to maintain the order of all Keys Accessed, LRU near Tail
        
        self.head = DLLnode(-1, -1)
        self.tail = DLLnode(-1, -1)
        self.head.next = self.tail
        self.tail.previous = self.head
        
    def addToHead(self, node):
        node.next = self.head.next
        self.head.next = node
        node.previous = self.head
        node.next.previous = node
        
    def deleteNode(self, node):
        node.previous.next = node.next
        node.next.previous = node.previous
        
    def get(self, key):
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # once accessed a node, it should be removed from its position and added to the head
        self.deleteNode(node)
        self.addToHead(node)
        return node.val

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            # we accessed the node => delete the node from DLL and add it to Head of DLL
            self.deleteNode(node)
            self.addToHead(node)

        else:
            node = DLLnode(key, value)

            # REDUCE SIZE IF CAPACITY REACHED TO CREATE SPACE BEFORE ADDING THE NEW NODE
            if self.size == self.capacity:     
                del self.cache[self.tail.previous.key]
                self.deleteNode(self.tail.previous)
                self.size -= 1 

            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
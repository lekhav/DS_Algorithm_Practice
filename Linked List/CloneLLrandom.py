
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution1_Iterative:
    # HASHMAP SOLUTION
    # O[N] Time, O[N] Space
    def copyRandomList(self, head):
        if head == None:
            return None
        
        # 1) create a cloned node with Val for every node, store it in a map
        self.visitedMap = {}
        old_node = head
        new_node = Node(head.val)
        self.visitedMap[old_node] = new_node
        
        while old_node != None:
            # 2) Assign Next node for the cloned node,
            new_node.next = self.clonedNode(old_node.next)
            # 3) Assign Random node for the cloned node,
            new_node.random = self.clonedNode(old_node.random)
            
            old_node = old_node.next
            new_node = new_node.next
        return self.visitedMap[head]
    
    def clonedNode(self, node):
        if node == None:
            return None
        
        if node not in self.visitedMap:
            self.visitedMap[node] = Node(node.val)
        return self.visitedMap[node]



class Solution1_Recursive:
    
    # O[N] time; O[N] space
    def __init__(self):
        self.visitedHash = {}            # { OriginalNode: ClonedNode }
        
    def copyRandomList(self, head):
        if head == None:
            return None
        if head in self.visitedHash:
            return self.visitedHash[head]

        node = Node(head.val, None, None)
        self.visitedHash[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node



class Solution2:
    # InterLeaving the Cloned nodes after every node,
    # O[3N] Time
    # O[1] Space
    def copyRandomList(self, head):
        if head == None:
            return None
        
        # 1) Iterate over the original node, Insert a Cloned node next to every Original Node with its val
        # 2) Assign the Next pointer for the cloned node
        old_ll = head
        while old_ll != None:
            new_ll = Node(old_ll.val, None, None)
            new_ll.next = old_ll.next
            old_ll.next = new_ll
            old_ll = new_ll.next

        # 3) Iterate from the begining, Assign the Random pointer for the cloned nodes
        ptr = head
        while ptr != None:
            ptr.next.random = ptr.random.next if ptr.random else None #***********
            ptr = ptr.next.next

        # Iterate from the begining, Un-Weiving the LL to the Original LL and Cloned LL
        old_ll = head
        result = new_ll = head.next
        while old_ll != None:
            old_ll.next = old_ll.next.next
            new_ll.next = new_ll.next.next if new_ll.next != None else None
            old_ll = old_ll.next
            new_ll = new_ll.next
        return result
        







d = {}
d[(1, 8)] = 50
for key in d:
    print(key[0])

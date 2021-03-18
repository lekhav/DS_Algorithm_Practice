class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


# BRUTEFORCE: O[N] Time, O[N] Space
# push all Nodes into a set and if node already exists in set, return Node



# OPTIMIZED SOLUTION - Tortoise & Heir Algorithm
# O[2N] Time, O[1] Space
class Solution:
    def detectCycle(self, head):

        # EDGE CASE
        if head == None or head.next == None:
            return None

        slow = head
        fast = head
        flag = False
        while fast != None and fast.next != None:     # Find if Cycle is present
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break

        if flag == False:      # No Cycle Detected, return None
            return None
                      
        slow = head            # Cycle Detected, return Node by Floyd's Tortoise Heir ALGO
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
         
    




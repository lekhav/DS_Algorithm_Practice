# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):
        if head == None or head.next == None:
            return None


        # finding the midpoint by Floyd's Tortoise-Heir Algorithm,   O[N] Time
        # breaking the LL into 2 halves, and reversing the second half,     O[N/2] Time   
        result = l1 = head
        mid = self.findMid(head)
        
        l2 = mid.next
        mid.next = None
        l2 = self.reverseLL(l2)
        
        # reordering the LL 
        dummy = ListNode(-1)
        while l1 != None and l2 != None:
            dummy.next = l1
            l1 = l1.next
            dummy = dummy.next
            
            dummy.next = l2
            l2 = l2.next
            dummy = dummy.next
        if l1 != None:
            dummy.next = l1
        elif l2 != None:
            dummy.next = l2
        return result
            
        
        
    
    def findMid(self, head):
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseLL(self, head):
        if head == None or head.next == None:
            return head
        previous = None
        current = head
        fast = head.next
        while current.next != None:
            current.next = previous
            previous = current
            current = fast
            fast = fast.next
        current.next = previous
        return current
        
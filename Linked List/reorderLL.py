# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O[2N] time, O[1] space
    def reorderList(self, head):
        if head == None:
            return 
        
        # finding the midpoint by Floyd's Tortoise-Heir Algorithm,   
        # => O[N] Time
        mid = self.midPoint(head)
        
        # breaking the LL into 2 halves, and reversing the second half 
        # => O[N/2] Time
        l2 = mid.next
        mid.next = None
        l2 = self.reverse(l2)                               
        l1 = temp = head
        
        # reordering the LL,  
        # => O[N/2] Time
        while l1.next != None and l2 != None:
            temp = l1.next
            l1.next = l2
            l2 = l2.next 
            l1.next.next = temp 
            l1 = temp
        return head
            
    # -----------------------------------------------------------  
    def midPoint(self, head):
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow 

    def reverse(self, head):
        if not head:
            return None
        
        dummy = None
        slow = head
        fast = head.next   
        while slow.next != None:
            slow.next = dummy
            dummy = slow  
            slow = fast
            fast = fast.next
        slow.next = dummy
        return slow  
    
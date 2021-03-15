# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        result = current = ListNode(-1)
        
        while l1 != None or l2 != None or carry != 0:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            current.next = ListNode(carry%10)
            carry = carry//10
            current = current.next
        return result.next
            
                
        
        
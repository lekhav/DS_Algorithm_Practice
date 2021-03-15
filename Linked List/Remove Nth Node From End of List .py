# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        if head ==  None:
            return None

        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy
        
        for i in range(n):
            fast = fast.next
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next

class Solution:
    def removeNthFromEnd(self, head, n):
        if n == 1 and head.next == None:
            return None
        
        result = head
        l = 0                        # find the length
        while head != None:
            head = head.next
            l +=1

        head = result               # reset the head and move the head for l-n-1
        if l == n:    
            return result.next
        while l-n-1 > 0:       
            head = head.next
            l -= 1
        head.next = head.next.next    # delete the netx node and return result
        return result

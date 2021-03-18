# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    # O[3N] Time
    def removeNthFromEnd(self, head, n):
        r = dummy = ListNode(-1)
        dummy.next = self.reverseList(head)

        for i in range(n-1):
            dummy = dummy.next
        if dummy.next != None:
            dummy.next = dummy.next.next
        
        result = self.reverseList(r.next)
        return result
        

    # Reverse the LL, Delete the Nth node, Reverse the LL again
    def reverseList(self, head):
        if not head:
            return
            
        slow = None    
        current = head
        fast = head.next
        
        while current.next != None:
            current.next = slow
            slow = current
            current = fast
            fast = fast.next
        current.next = slow
        return current

    

class Solution2:
    # O[3N] Time
    # find the Length of LL, reset the head and move the head for l-n-1, Delete the next node and return result

    def removeNthFromEnd(self, head, n):
        result = head
        l = 0                         
        while head != None:
            head = head.next
            l +=1

        head = result                 
        if l == n:    
            return result.next
        while l-n-1 > 0:       
            head = head.next
            l -= 1
        head.next = head.next.next    
        return result

class Solution3:
    # OPTIMIZED SOLUTION - FLOYD's Algorithm 
    # O[N] Time
    def removeNthFromEnd(self, head, n):
        if head ==  None:
            return None

        dummy = ListNode(-1)         #  ****************  #
        dummy.next = head
        slow, fast = dummy, dummy
        
        for i in range(n):
            fast = fast.next
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next





    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(N+M) time, O(N+M) space
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return
        s = set()
        while headA != None:
            s.add(headA)
            headA = headA.next   
        while headB != None:
            if headB in s:
                return headB
            headB = headB.next
 

    def getIntersectionNode(self, headA, headB):
        # O(N+M) time
        # O(1) space
        if headA == None or headB == None:
            return 

        # FIND THE LENGTH OF THE TWO LISTS
        lenA, lenB = 0, 0
        temp = headA
        while temp != None:
            lenA += 1
            temp = temp.next
        temp = headB
        while temp != None:
            lenB += 1
            temp = temp.next
        
        # MOVE THE STARTING POINTER ON THE LONGER LIST BY, lenA - lenB
        if lenA - lenB > 0:
            diff = lenA - lenB
            while diff != 0:
                headA = headA.next
                diff -= 1
        else:
            diff = lenB - lenA
            while diff != 0:
                headB = headB.next
                diff -= 1
                
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
        
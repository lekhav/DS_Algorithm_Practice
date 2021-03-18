
class ListNode:
    def __init__(self, key):
        self.val = key
        self.next = None


class Solution:
    # Time : O(N*K), N: avg.no.of.nodes/linkedlist, K: no.of.linkedlist
    # Space: O(N) to store result LL

    def mergeKLists(self, lists):
        if lists == None or len(lists) == 0:
            return None
        
        result = merged = ListNode(float('-inf'))
        for head in lists:
            merged = self.mergeTwoLists(merged, head)
        return result.next
            

    def mergeTwoLists(self, l1, l2):
        # EDGE CASE
        if l1 == None and l2 == None:
            return None

        result = dummy = ListNode(0)
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next= l2
                l2 = l2.next
            dummy = dummy.next

        if l1 != None:
            dummy.next = l1
        else:
            dummy.next = l2
            
        return result.next
    

#========================================================================================================
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class SolutionOPTIMIZED:
    import heapq

    # O[NlogK] Time
    # O[K] Space for Heapq + O[N] for Result LL
    def mergeKLists(self, lists):
        if lists == []:
            return None
        
        # Maintain a MinHeap of all the 1t nodes in the Lists        
        minHeap = []
        heapq.heapify(minHeap)
        for i in range(len(lists)):
            if lists[i] != None:
                heapq.heappush(minHeap, (lists[i].val, i, lists[i]))
        
        result = merged = ListNode(-1)
        while minHeap != []:
            poppedVal, index, poppedNode = heapq.heappop(minHeap)
            merged.next = poppedNode
            merged = merged.next
            nextNode = poppedNode.next
            if nextNode != None:
                heapq.heappush(minHeap, (nextNode.val, index, nextNode))
        return result.next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        if root == None:
            return True
        
        st = []
        previous = None
        while root != None or st != []:
            while root != None:
                st.append(root)
                root = root.left
            root = st.pop()
            if previous != None and root.val <= previous:
                return False
            
            previous = root.val
            root = root.right
        return True
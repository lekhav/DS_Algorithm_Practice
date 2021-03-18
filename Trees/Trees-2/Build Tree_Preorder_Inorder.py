# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree_Iterative(self, preorder, inorder):
        if preorder == []:
            return None
        
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        
        preorderLeft = preorder[1:index+1]
        preorderRight = preorder[index+1:]
        inorderLeft = inorder[:index]
        inorderRight = inorder[index+1:]
        
        root.left = self.buildTree(preorderLeft, inorderLeft)
        root.right = self.buildTree(preorderRight, inorderRight)
        return root


class Solution:
    def buildTree_Recursive(self, preorder, inorder):
        # BASE CASE
        if preorder == [] or len(inorder) == 0:
            return None
        
        # LOGIC
        root = TreeNode(preorder.pop(0))
        index = inorder.index(root.val)
        
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index+1:])
        return root
    
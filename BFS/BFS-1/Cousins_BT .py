# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.x_parent = None
        self.y_parent = None
        self.x_depth = None
        self.y_depth = None
        self.dfs(root, x, y, 0, None)
        
        if self.x_depth == self.y_depth and self.x_parent != self.y_parent:
            return True
        return False
    
    def dfs(self, root, x, y, depth, parent):
        # BASE CASE
        if root == None:
            return
        if root.val == x:
            self.x_depth = depth
            self.x_parent = parent
        if root.val == y:
            self.y_depth = depth
            self.y_parent = parent
            
        # LOGIC
        self.dfs(root.left, x, y, depth+1, root)
        self.dfs(root.right, x, y, depth+1, root)
        


    # ----------------------------------------------------------------------------------
    def isCousins(self, root, x, y):
        depth, x_depth, y_depth = 0, 0, 0
        x_parent, y_parent = None, None
        
        stack = []
        while root != None or stack != []:
            while root != None:
                stack.append([root, depth])
                if root.left != None:
                    if root.left.val == x:
                        x_depth, x_parent = depth+1, root
                    elif root.left.val == y:
                        y_depth, y_parent = depth+1, root
                root = root.left
                depth += 1
                
            root, depth = stack.pop()
            if root.right != None:
                if root.right.val == x:
                    x_depth, x_parent = depth+1, root
                elif root.right.val == y:
                    y_depth, y_parent = depth+1, root
            root = root.right
            depth += 1
        
        if x_depth == y_depth and x_parent != y_parent:
            return True
        return False
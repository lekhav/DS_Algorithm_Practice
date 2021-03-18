
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # BFS APPROACH: level order traversal and add the last element of each level to result
    # time : O(N)
    # space: O(N) in WORST CASE: N nodes in the right view 

    def rightSideView(self, root):
        if root == None:
            return []
        
        rightView = []
        q = [root]
        while q != []:
            l = len(q)
            for i in range(l):
                root = q.pop(0)
                if root.left != None:
                    q.append(root.left)
                if root.right != None:
                    q.append(root.right)
                if i == l-1:                       # i = 0, gives the LeftView
                    rightView.append(root.val)
        return rightView


    # DFS APPROACH: 
    # time : O(N)
    # space : O(1) + Recursive call stack
    def rightSideView(self, root):
        if root == None:
            return []
        
        # DFS Approach
        self.result = [root.val]
        self.dfs(root, 1)
        return self.result
    
    def dfs(self, root, depth):
        # BASE CASE
        if root == None:
            return
        
        # LOGIC
        if depth > len(self.result):
            self.result.append(root.val)
        if root.right:
            self.dfs(root.right, depth+1)
        if root.left:
            self.dfs(root.left, depth+1)




a = TreeNode(3)
a.left = TreeNode(9)
a.left.left = TreeNode(1)
a.left.right = TreeNode(0)
a.right = TreeNode(20)
a.right.left = TreeNode(15)
a.right.right = TreeNode(7)

obj = Solution()
print(obj.rightSideView(root=a))

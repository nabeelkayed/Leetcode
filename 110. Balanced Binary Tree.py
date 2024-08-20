# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        
        def isBalanced(root):
            if root == None:
                return True
            if root.left == None and root.right == None:
                return 1
            
            left = 0
            right = 0
            if root.left != None:
                left = isBalanced(root.left)
            if root.right != None:
                right = isBalanced(root.right)
            if abs(left - right) > 1:
                self.balanced = False 
            return max(left, right) + 1    
        isBalanced(root)
        return self.balanced

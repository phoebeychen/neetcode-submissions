# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def treeHeight(node: Optional[TreeNode]) -> int:

            if not node:
                return 0
            leftHeight = treeHeight(node.left)
            rightHeight = treeHeight(node.right)
            
            return 1 + max(leftHeight, rightHeight)
            
       
        left = treeHeight(root.left)
        right = treeHeight(root.right)
        
        if abs(left - right) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
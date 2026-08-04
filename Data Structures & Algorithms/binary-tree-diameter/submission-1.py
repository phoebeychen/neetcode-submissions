# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      # 对任意节点，该节点的最长路径 = 左子树的最大高度 + 右子树的最大高度

        if not root:
            return 0
    
        def maxHeight(node):
            if not node:
                return 0
            
            return 1 + max(maxHeight(node.left), maxHeight(node.right))
        
        
        leftHeight = maxHeight(root.left)
        rightHeight = maxHeight(root.right)
        d = leftHeight + rightHeight # root's d

        # root.left's d  root.right 's d
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return max(d, sub)



        

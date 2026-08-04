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
        res = 0

        def maxHeight(node):
            nonlocal res

            if not node:
                return 0
            
            leftHeight = maxHeight(node.left)
            rightHeight = maxHeight(node.right)

            d = leftHeight + rightHeight

            res = max(res, d)

            return 1 + max(leftHeight, rightHeight)
        
        maxHeight(root)

        return res
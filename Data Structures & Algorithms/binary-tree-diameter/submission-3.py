# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      # 对任意节点，该节点的最长路径 = 左子树的最大高度 + 右子树的最大高度

        res = 0

        if not root:
            return res
        
        def dfs(node):

            nonlocal res

            if not node:
                return 0
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            res = max(res, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)

        dfs(root)

        return res

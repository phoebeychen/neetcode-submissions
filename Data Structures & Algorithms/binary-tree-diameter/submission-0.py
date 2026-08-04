# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      # 对任意节点，该节点的最长路径 = 左子树的高度 + 右子树的高度

        if not root:
            return 0
        
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        l_height = height(root.left)
        r_height = height(root.right)

        d = l_height + r_height # root 节点的最长路径

        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return max(sub, d)

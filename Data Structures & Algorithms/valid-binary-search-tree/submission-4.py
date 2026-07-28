# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        if not root:
            return None

        queue = deque([(root, float("-inf"), float("inf"))]) # 每个节点在进入队列时，必须“携带”它自己的左右边界。

        while queue:
            node, low, high = queue.popleft()
            
            if not (low < node.val < high):
                return False

            if node.left:
                queue.append((node.left, low, node.val))

            if node.right:
                queue.append((node.right,node.val, high))

        return True
    
            
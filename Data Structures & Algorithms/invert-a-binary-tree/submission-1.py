# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque # 新数据结构，BFS经常用
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        queue = deque([root]) # # 创建双端队列，初始放入根节点，实现FIFO
        while queue:
            node = queue.popleft() # deque.popleft() 很快 O(1)

            if node.left: # node 有左节点
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            node.left, node.right = node.right, node.left
        return root



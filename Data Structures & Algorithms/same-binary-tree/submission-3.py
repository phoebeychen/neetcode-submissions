# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        
        queue = deque([(p,q)]) # 输入元组的时候记得加括号,()里的东西算一个元素

        while queue:
            nodeP, nodeQ = queue.popleft()

            if not nodeP and not nodeQ:
                continue
            if not nodeP or not nodeQ or nodeP.val != nodeQ.val:
                return False
            
            queue.append((nodeP.left, nodeQ.left))
            queue.append((nodeP.right, nodeQ.right))
        
        return True

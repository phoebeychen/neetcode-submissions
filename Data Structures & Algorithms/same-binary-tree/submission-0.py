# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            left_result = self.isSameTree(p.left,q.left)
            right_result = self.isSameTree(p.right, q.right)
            return left_result and right_result
        else:
            return False


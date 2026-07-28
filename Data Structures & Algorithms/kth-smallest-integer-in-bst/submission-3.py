# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        cnt = k
        res = root.val

        def inorder(node):
            nonlocal cnt, res # 在局部函数里修改不可变的全局变量的时候要用nonlocal声明，如果只读不需要nonlocal声明

            if not node:
                return None

            inorder(node.left)

            # if cnt == 0: # 如果上面递归左边之后cnt已经为0，返回这一层的则直接返回
            #     return

            cnt -= 1 # 每经过一个节点，计数器就-1
            if cnt == 0: # 当计数器降到0时，当前节点就是我们要找的答案
                res = node.val
                return res

            inorder(node.right)

        inorder(root)
        return res
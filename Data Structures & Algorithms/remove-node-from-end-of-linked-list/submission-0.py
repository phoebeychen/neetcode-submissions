# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        removeIndex = len(nodes) - n # 转换成数组是因为列表没有能直接计算长度的函数吗？

        if not removeIndex:
            return head.next
        else:
            nodes[removeIndex - 1].next = nodes[removeIndex].next
            return head


        
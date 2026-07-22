# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 把链表当数组处理，可以通过len()-n 正面计算坐标位置，然后对用下标对数组取值
# O(n), O(n)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        curr = head
        while curr:
            N += 1
            curr = curr.next
        
        removeIndex = N - n

        if not removeIndex:
            return head.next
        else:
            curr = head # 从头开始遍历链表
            for i in range(N-1): # 为什么是N-1 不是N？
                if (i + 1) == removeIndex:
                    curr.next = curr.next.next
                    break # 这里被我直接return掉了
                curr = curr.next
            return head


        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        if not headA or not headB:
            return None
        
        pA = headA
        pB = headB

        
        while pA != pB: # 判断条件写错了
            if pA: # if 条件也写错了
                pA = pA.next
            else:
                pA = headB
            if pB:
                pB = pB.next
            else:
                pB = headA

        return pA
        
        # while pA:
        #     pA = pA.next
        #     if pA == 0:
        #         pA = headB
        
        # while pB:
        #     pB = pB.next
        #     if pB == 0:
        #         PB = headA
        
        # if pA == PB:
        #     return pA
        # else:
        #     return None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set() # 第一次写写成了defaultdict 搞不懂字典和集合的区别啊阿啊
        curr = head
        while curr:
            seen.add(curr) # dict 可以存指针？
            curr = curr.next
            if curr in seen:
                return True
        return False
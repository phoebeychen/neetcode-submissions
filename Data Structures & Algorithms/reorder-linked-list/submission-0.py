# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        mid = slow.next # mid 为啥不等于slow，而是slow.next
        slow.next = None # 列表需要分割开

        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            pre = None
            curr = head

            while curr:
                temp = curr.next
                curr.next = pre # 往左指
                pre = curr
                curr = temp
            return pre

        tail = reverseList(mid)

        while tail:
            next_head = head.next
            next_tail = tail.next

            head.next = tail
            tail.next = next_head

            head = next_head
            tail = next_tail
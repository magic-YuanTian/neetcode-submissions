# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return None

        fast = head

        cnt = 0
        for i in range(n):
            fast = fast.next
            cnt += 1
            if not fast:
                break
        
        if not fast:
            return head.next

        slow = head

        while fast.next:
            fast = fast.next
            slow = slow.next
        
        temp = slow.next
        slow.next = slow.next.next
        temp.next = None

        return head
        
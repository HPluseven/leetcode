# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        pre = None
        cur = head

        while cur:
            if pre and pre.val == cur.val:
                pre.next = cur.next
            else:
                pre = cur
            
            cur = cur.next
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        chk = set()
        cur = head
        while cur and cur not in chk:
            chk.add(cur)
            cur = cur.next
        return cur
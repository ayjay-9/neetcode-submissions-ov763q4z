# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr, nxt = head, head
        while curr:
            if nxt.next:
                if nxt.next.next is None:
                    break
                else:
                    nxt = nxt.next.next
            else:
                break
            curr = curr.next
            if nxt == curr:
                return True
        return False
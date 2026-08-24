# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # e.g Return the 2nd Node from the end of the list, not 2nd index
        dummy = ListNode(0, head) # dummy(0) -> 1 -> 2 -> 3 -> None
        fast = dummy
        slow = dummy
        for _ in range(n): # If n = 2 fast stops at 2, dummy(0) -> 1 -> 2(fast) -> 3 -> None
            fast = fast.next

        while fast.next: # dummy(0) -> 1(slow) -> 2 -> 3(fast) -> None
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next # 1.next == 2, so it now becomes 1.next == 2.next
        # dummy(0) -> 1(slow) -> 3(fast) -> None
        return dummy.next # 1(slow) -> 3(fast) -> None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # General Reorder [0, n-1, 1, n-2, 2, n-3, ...]
        # Find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next # This will stop at the middle when fast gets to the end
            fast = fast.next.next

        # Reverse the second half of the list, node after middle (where slow stopped)
        second = slow.next # starts at the node immediately after middle
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Merge both halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
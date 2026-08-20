# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = list1, list2
        merged_list = ListNode()
        tail = merged_list
        while h1 or h2:
            if h1:
                if h2:
                    if h1.val <= h2.val:
                        tail.next = ListNode(h1.val)
                        h1 = h1.next
                    else:
                        tail.next = ListNode(h2.val)
                        h2 = h2.next
                else:
                    tail.next = ListNode(h1.val)
                    h1 = h1.next
            else:
                if h2:
                    tail.next = ListNode(h2.val)
                    h2 = h2.next
            tail = tail.next
        return merged_list.next
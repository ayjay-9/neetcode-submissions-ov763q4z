# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
           return None

        q = deque([root])
        stack = [root.val]
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    stack.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    stack.append(node.right.val)
        stack.sort()
        return stack[k-1]
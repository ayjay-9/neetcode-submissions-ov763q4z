# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        self.max_val = float('-inf')
        def dfs(curr: TreeNode) -> int:
            if not curr:
                return 0

            left_max, right_max = 0, 0
            if curr.left:
                left_max = max(0, dfs(curr.left))

            if curr.right:
                right_max = max(0, dfs(curr.right))

            self.max_val = max(self.max_val, curr.val+left_max+right_max)
            return curr.val + max(left_max, right_max)
        dfs(root)
        return self.max_val
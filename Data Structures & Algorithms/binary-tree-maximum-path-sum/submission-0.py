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
        res = [root.val]
        def dfs(curr: TreeNode) -> int:
            if not curr:
                return 0

            left_max, right_max = dfs(curr.left), dfs(curr.right)
            left_max, right_max = max(left_max, 0), max(right_max, 0)

            res[0] = max(res[0], curr.val+left_max+right_max)
            return curr.val + max(left_max, right_max)
        dfs(root)
        return res[0]
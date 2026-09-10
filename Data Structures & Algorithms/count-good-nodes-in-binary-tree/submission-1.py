# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        if not root:
            return self.count
        else:
            self.prev = root.val
        def dfs(curr: TreeNode):
            if not curr:
                return

            old_val = self.prev

            if curr.val >= self.prev:
                self.count += 1
                self.prev = curr.val
                
            dfs(curr.left)
            dfs(curr.right)

            self.prev = old_val

        dfs(root)
        return self.count
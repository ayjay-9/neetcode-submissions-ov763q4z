# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Height(Left) - Height(Right) = [-1,0,1]
        self.res = True
        if not root:
            return self.res # Base case if no root, then no left and right subtrees
        def dfs(curr: TreeNode) -> int:
            if not curr:
                return 0 # If no subtree
            # Find the heights of the subtrees
            left, right = dfs(curr.left), dfs(curr.right)
            if abs(left - right) > 1:
                self.res = False
            return 1 + max(left,right) # Return the height
        dfs(root)
        return self.res
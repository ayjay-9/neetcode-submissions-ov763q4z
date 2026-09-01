# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0 # Initial diameter
        def dfs(curr: Optional[Treenode]) -> int:
            if not curr:
                return 0
            left, right = dfs(curr.left), dfs(curr.right) # Find the height of left and right subtrees
            self.diameter = max(self.diameter, left+right) # Deepest left -> Current -> Deepest right = left + right
            return 1 + max(left,right) # Return the height
        dfs(root) # Start from root node
        return self.diameter
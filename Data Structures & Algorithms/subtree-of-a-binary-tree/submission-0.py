# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(a: TreeNode, b: TreeNode) -> bool:
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return sameTree(a.left, b.left) and sameTree(a.right, b.right)

        def dfs(curr_root: TreeNode) -> bool:
            if not curr_root:
                return False
            if sameTree(curr_root, subRoot):
                return True
            return dfs(curr_root.left) or dfs(curr_root.right)

        return dfs(root)
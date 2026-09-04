# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Faster to find ancestors of descendants on the same side of the tree
        # Descendant can be the ancestor of itself
        self.lca = root
        if (p.val < root.val < q.val) or (q.val < root.val < p.val): # LCA is root
            return self.lca

        def dfs(curr: TreeNode) -> TreeNode:
            if not curr:
                return None
            if p.val < curr.val and q.val < curr.val: # LCA is on left, recurse the left
                dfs(curr.left)
            if p.val > curr.val and q.val > curr.val: # LCA is on right, recurse right
                dfs(curr.right)

            if (p.val < curr.val < q.val) or (q.val < curr.val < p.val): # The lca is the root
                self.lca = curr
                return self.lca
            if p.val == curr.val:
                self.lca = p
                return self.lca
            if q.val == curr.val:
                self.lca = q
                return self.lca

            return dfs(curr.left) or dfs(curr.right)
        dfs(root)
        return self.lca
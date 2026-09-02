# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.equal = True # Default is no root, so no children
        # If both don't have a root
        if not p and not q:
            return self.equal
        # If either doesn't have a root, then they are unequal
        if p and not q:
            return False
        if q and not p:
            return False
        # Check if subtrees on left and right are the same
        def dfs(p_curr: TreeNode, q_curr: TreeNode) -> bool:
            if not p_curr and not q_curr: # If both are Null, they are equal
                self.equal = True
                return self.equal
            if (not p_curr and q_curr) or (p_curr and not q_curr): # If either one of them is Null, they are not equal
                self.equal = False
                return self.equal
            if p_curr.val != q_curr.val: # If Nodes don't have the same number, they are not equal
                self.equal = False
                return self.equal

            left, right = dfs(p_curr.left, q_curr.left), dfs(p_curr.right, q_curr.right)

            if not left or not right:
                self.equal = False

            return p_curr.val == q_curr.val
        dfs(p, q)
        return self.equal
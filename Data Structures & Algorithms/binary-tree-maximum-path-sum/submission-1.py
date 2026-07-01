# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi=-math.inf
        def trav(root):
            nonlocal maxi
            if root is None:
                return 0
            l=trav(root.left)
            r=trav(root.right)
            maxi=max(l+root.val,r+root.val,l+r+root.val,root.val,maxi)
            return max(root.val,root.val+l,root.val+r)
        trav(root)
        return maxi


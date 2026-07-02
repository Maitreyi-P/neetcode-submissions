# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxval = -math.inf
        def rec(root):
            nonlocal maxval
            if not root:
                return 0

            leftsum = rec(root.left)
            rightsum = rec(root.right)
            maxval = max(maxval, leftsum + root.val, rightsum+root.val, root.val, leftsum+rightsum+root.val)

            return max(leftsum+ root.val, rightsum+root.val, root.val)

        rec(root)
        return maxval
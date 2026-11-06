# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        rangesum = 0

        def dfs(node):
            nonlocal rangesum
            if not node:
                return  0
            if node.val > high:
                return dfs(node.left)
            if node.val < low:
                return dfs(node.right)

            rangesum += node.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return rangesum
            
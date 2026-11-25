# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        def lca(root,p,q):
            if not root or root == p or root == q:
                return root
            
            left = lca(root.left, p,q)
            right = lca(root.right, p,q)

            if left and right:
                return root
            if left:
                return left
            return right

        return lca(root,p,q)

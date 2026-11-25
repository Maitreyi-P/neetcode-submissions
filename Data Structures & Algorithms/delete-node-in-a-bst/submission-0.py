# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def dfs(node,key):
            if not node:
                return None

            if node.val < key:
                node.right = dfs(node.right,key)

            elif node.val > key:
                node.left = dfs(node.left,key)

            else:
                #no left child
                if not node.left:
                    return node.right
                #no right child
                if not node.right:
                    return node.left
                #children 
                succ = node.right
                while succ.left:
                    succ = succ.left
                
                node.val = succ.val
                node.right = dfs(node.right, succ.val)

            
            return node

        return dfs(root,key)
                

            

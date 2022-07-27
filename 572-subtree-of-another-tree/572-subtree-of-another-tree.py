# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def IsSame(r , s):
            if not r and not s:
                return True
            
            if r and s and r.val == s.val:
                return IsSame(r.left , s.left) and IsSame(r.right , s.right)
            
        def SubTree(root , sub):
            if not root : return False
            if not sub : return True
            
            if IsSame(root  , sub):
                return True
            
            return SubTree(root.left , sub) or SubTree(root.right, sub)
        
        return SubTree(root , subRoot)
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def LeftHeight(root):
            lh =0
            if not root:
                return lh
            while root:
                lh+=1
                root = root.left
            return lh
        
        def RightHeight(root):
            rh=0
            if not root:
                return rh
            while root:
                rh+=1
                root = root.right
            return rh
                        
        def TotalCompleteNodes(root):
            if not root:
                return 0
            
            left = LeftHeight(root)
            right = RightHeight(root)
                        
            if left == right:
                return (2**left)-1
            
            return 1+TotalCompleteNodes(root.left) + TotalCompleteNodes(root.right)
                        
                        
        return TotalCompleteNodes(root)
        
        
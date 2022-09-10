# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def preorder(root , res):
            if not root:
                return
            
            res.add(root.val)
            preorder(root.left, res)
            preorder(root.right, res)
            
            
        res = set()
        
        preorder(root , res)
        min1 , ans = root.val , float('inf')
        
        for v in res:
            if min1 < v < ans:
                ans = v
        
        return ans if ans < float('inf') else -1
       
            
        
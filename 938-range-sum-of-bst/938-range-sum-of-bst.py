# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0 
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def SumRange(root , low, high):
            if not root:
                return
            if root.val>=low and root.val<=high:
                self.res+=root.val
                
            if root.left:
                SumRange(root.left, low, high)
            if root.right:
                SumRange(root.right, low, high)
                
        SumRange(root, low, high)
        return self.res
        
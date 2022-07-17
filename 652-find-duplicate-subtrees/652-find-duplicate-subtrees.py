# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        def dfs(root , mp):
            if not root:
                return "#"
            
            l = dfs(root.left, mp)
            r = dfs(root.right, mp)
            
            s = str(root.val) + '#' + l + '#' + r
            
            mp[s]+=1
            
            if mp[s]==2:
                res.append(root)
            
            
            return s
                
        mp = defaultdict(int)
        dfs(root, mp)
        return res
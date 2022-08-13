# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def inorderTrav(root1, target, res):
            if not root1:
                return
            inorderTrav(root1.left , target, res)
            res.append(target - root1.val)
            inorderTrav(root1.right , target , res)


        def findTarget(root2, res):
            st = []
            while st or root2:

                while root2:
                    st.append(root2)
                    root2 =root2.left

                node = st.pop()
                if node.val in res:
                    return True
                
                root2 =  node.right

            return False
            
            

        res =[]
        inorderTrav(root1, target, res)
        v = findTarget(root2, res)
        return v
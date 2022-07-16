# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        st = []
        node= root
        total =0
        while st or node is not None:
            
            while node is not None:
                st.append(node)
                node = node.right

            node = st.pop()
            total+=node.val
            node.val = total

            node = node.left
            
        return root
    
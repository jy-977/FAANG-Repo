# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #recursion 62ms 23.2% / 13.9mb 59.96% lesss
        def invert (root) : 
            if root : 
                root.left ,root.right = root.right, root.left
                invert(root.left)
                invert(root.right)
            return root
        return invert(root)
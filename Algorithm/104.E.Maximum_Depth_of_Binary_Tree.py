# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #dfs 43ms 94.48, 16.3mb 23.40 less
        #dfs 깊이 확인 max(ld, rd ) + 
        
        d = 0
        def depth (r) :
            if r : 
                ld , rd = 0,0
                if(r.left) : 
                    ld = depth(r.left)
                if(r.right) : 
                    rd = depth(r.right)
                return max(ld,rd)+1
        res =  depth(root)
        return res if res else 0
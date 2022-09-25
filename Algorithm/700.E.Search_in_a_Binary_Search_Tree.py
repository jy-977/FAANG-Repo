# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #problem analysis
        # understanding : return the node that has the same value with input "val" and subtree of finding value : 
        
        
#idea 1) recursion : 184ms 8.62% faster / 16.6mb 24.89% less
#         if root : 
#             if root.val == val : return root
            
#             if val < root.val : return self.searchBST(root.left, val)
#             else : return self.searchBST(root.right, val)
#         else : 
#             return 

# solution 1) iteratio 151ms 29.94% faster / 16.5mb 70.07 less
        while root : 
            if(root.val == val ) : return root
            
            if(val< root.val) : 
                root = root.left
                continue 
            elif ( val > root.val ) : 
                root = root.right
                continue 
                
#review 
#트리 search 기본 방법 두개 
# 1) recursion 2) iteration
# root 있는지 항상 확인

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
     
    
    
    
    #idea 1) recursion
        # if(root) : 
        #     if (root.left) : 
        #         if root.left.val>=root.val : return False
        #         if not self.isValidBST(root.left) : return False
        #     if root.right :
        #         if root.right.val <=root.val : return False
        #         if not self.isValidBST(root.right) : return False
        # return True
    
    #edge case 처리 매우매우 미흡,,,
    # left 에 right 보다 큰게 있으면 안됨
    #
    
# #    idea 2) iteration + stack : 1867ms 4.04% faster / 16.5mb 46.73 less
#         output = []
#         stack,p= [],root
#         while (p or stack) : 
#             if p : 
#                 stack.append(p) 
#                 if(p.left) : 
#                     if(p.left.val >= p.val) : return False
#                 p = p.left
#             else : 
#                 p =  stack.pop()
#                 if(output and max(output)>=p.val) : return False
#                 output.append(p.val)
#                 p = p.right
#         return True

# solution : recursion 91ms 23.9% faster / 16.4mb 93.51% less

            def validate(node, low=-math.inf, high=math.inf):
                # Empty trees are valid BSTs.
                if not node:
                    return True
                # The current node's value must be between low and high.
                if node.val <= low or node.val >= high:
                    return False

                # The left and right subtree must also be valid.
                return (validate(node.right, node.val, high) and
                       validate(node.left, low, node.val))
            return validate(root)

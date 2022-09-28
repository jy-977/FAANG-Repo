# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #tree 조지기... 
        #problem analysis 
        #1) return : inorder로 순회한 tree 의 값을 리스트로 반환
        
        
        #idea 1) recursion 79ms 5.18% faster / 14mb
        # T : O(n) / S O(n)
        # def inorder(root) : 
        #     return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        
        #idea 2) simplified recursion 60ms 26.83% faster / 13.9mb 59.55 less
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
        
        
        
#         #idea 2) iteration & stack
       
        #root 를 바로 이요아면 Nonetype // deque는 iteration type을 이용할 수 없다고 함
        
        output =[]
        stack, p = [], root
        while stack or p :
            if p:
                stack.append(p)
                p = p.left
            else : 
                p = stack.pop()
                output.append(p.val)
                p = p.right
        return output
#     # Iterative solution 2: use a stack and a pointer

#         def inorderTraversal(self, root):
#             in_order = []
#             stack, p = [], root
#             while stack or p:
#                 if p:
#                     stack.append(p)
#                     p = p.left
#                 else:
#                     p = stack.pop()
#                     in_order.append(p.val)
#                     p = p.right
#             return in_order
    
    
    
            
        #review tree 순환 방법 알아놓기 : 중요~!
        # def preorder(root):
        #   return [root.val] + preorder(root.left) + preorder(root.right) if root else []
        # def inorder(root):
        #   return  inorder(root.left) + [root.val] + inorder(root.right) if root else []
        # def postorder(root):
        #   return  postorder(root.left) + postorder(root.right) + [root.val] if root else []
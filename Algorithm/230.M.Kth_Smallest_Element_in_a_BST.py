# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #problem analysis 
        
        
        
        
        #1) iteration? 
        # 1-1) output list 이용 : O(n) 120ms 12.51% faster / 18.1mb
        # 1-2) cnt 이용 : 100ms 35.74% faster / 18.2mb 17.5 less
        stack, p = [], root
        cnt = 0
        while(stack or p) : 
            if p : 
                stack.append(p)
                p = p.left
            else : 
                p = stack.pop()
                if(cnt==k-1) : 
                    return p.val
                p = p.right
                cnt+=1
    
        #2) recursion o(n) 119ms 13.37% / 18.3mb 5.71 less
#         def inorder(root) : 
#             return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        
#         return(inorder(root)[k-1])



#review : 정형화된 binary tree inorder 을 이용한 풀이 
#O(n)
        
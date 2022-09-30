# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        
        #recursion
        #문제이해잘못함 인접한 것들의 차이인줄 알았지 나는...!!!
        #나는 인접한 노드의 거리가 짧은걸 찾았다구..
        
#         def check (root,minout) : 
#             if root : 
#                 if root.left :
#                     minoutA = min( abs(root.val-root.left.val), check (root.left, minout))
#                 else  : minoutA = math.inf
#                 if root.right : 
#                     minoutB =  min( abs(root.val-root.right.val), check ( root.right, minout))
#                 else : minoutB = math.inf
#                 return min(minoutA, minoutB)
#         return check(root, math.inf)
  
        # #iteration 40ms 81.7- faster / 13.9mb 83.57 less
        minout = math.inf
        prev = math.inf
        stack , p= [], root
        while stack or p : 
            if p : 
                stack.append(p)
                p = p.left
            else :
                p = stack.pop()
                minout =min(minout, abs(prev- p.val))
                prev = p.val
                p = p.right
        return minout
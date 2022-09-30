# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        #iteration ------608ms 12.65% faster / 23.1 51.25% less----------------
        # out_sum = 0
        # stack, p = [], root
        # while stack or p  : 
        #     if p : 
        #         stack.append(p)
        #         p = p.left
        #     else : 
        #         p = stack.pop()
        #         if(low<=p.val<=high) : 
        #             out_sum+=p.val
        #         p= p.right
        # return out_sum
         
        #dfs 377ms 54.77% faster / 23mb 91.73 less
        out_sum = 0
        def dfs (root) :
            nonlocal out_sum
            if root : 
                if low<=root.val<=high:
                    print(root.val, out_sum)
                    out_sum+=root.val
                if low<=root.val :
                    dfs(root.left)
                if root.val<=high : 
                    dfs(root.right)
        dfs(root)
        return out_sum
    
        #REVIEW : 
        BST 새로운 접근법 DFS
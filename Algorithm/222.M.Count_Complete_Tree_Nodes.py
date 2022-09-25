# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # problem analysis 
        # 완전이진트리 : leaf는 아닐수 있음을 주의~
        # leaf 마지막 왼쪽은 또 complete.
        # node의 개수를 구하가
        #완전 이진트리라는 점이 뭘 더 시간을 줄이는데 도움이 되지 않을까..?
        
        #범위 굉장히 넓음.. 시간 걸릴거 같은데.. 어떻게 체크하는지 회고하기
        #
        
        
        #O(n) ==> 
        
    #idea 1) recursion +len(list) : 134ms 52.22% faster / 21.4 mb 46.40 less
    
#         def inorder (root:TreeNode) : 
#             return inorder(root.left) + [root.val] + inorder(root.right) if root else []
#         return len(inorder(root))
    

    #review : 
    #"완전 이진트리 " ==> binary search 가능
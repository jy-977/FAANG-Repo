# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
#idea 1)   #79ms 16.2 mb
#         if root :
#             if(target< root.val ) : 
#                 new = self.closestValue (root.left, target)
#             else : 
#                 new = self.closestValue (root.right, target)
#             if new == None : 
#                 return root.val
#             else : 
#                 if abs(root.val-target)<=abs(target - new) : 
#                     return root.val
#                 else : return new
#         else : return None
        
#solution 54ms 75.07% / 16.1mb 35.52% ================================================
#트리 순회 기본적인 내용임 그냥 외우자
#이 inorder 함수가 tree를 순차적으로 순회하여 list로 반환함

        def inorder(r : TreeNode) : 
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        new = inorder(root)
        return min(new, key = lambda x : abs(target - x))



#review +=================================================
#tree / linked list : 엣지케이스 처리 아직 많이 부족함
# root 가 있는지 root.next 가 있는지 항상확인


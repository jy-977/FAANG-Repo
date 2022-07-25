# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
#         def dfs (node1, node2) : 
#             print("node1 : ", node1.val,"node2 : ", node2.val)
# #             break point 
            
#             if not node1.left and not node1.right and  not node2.left and not node2.right :
#                 print("break 2")
#                 return
#             if(node2==None):
#                 print("break 3")
#                 return
# #             main action
           

# #           오른쪽 트리 채우기
#             if(node2.left and not node1.left) :
#                 newLeft = TreeNode()
#                 node1.left = newLeft
#             elif (node2.right and not node2.left) : 
#                 newRight = TreeNode()
#                 node1.right = newRight
            
# #           왼쪽트리
#             if(node2.left and node2.right) : 
#                 dfs(node1.left, node2.left)
#                 dfs(node1.right, node2.right)
#             elif(node2.left):
#                 dfs(node1.left, node2.left)
#                 dfs(nod1.right, None)
#             elif(node2.right):
#                 dfs(node1.left, None)
#                 dfs(nod1.right, node2.right)    
        
        
#         dfs(root1, root2)

#         def dfs (newTree, node1, node2):
#             print(newTree)
#             newTree.val = node1.val + node2.val
#             newTree.left = dfs(newTree.left, node1.left, node2.left)
#             newTree.right = dfs(newTree.right, node1.right, node2.right)
            
            if(root1 and root2) : 
                tree = TreeNode(root1.val + root2.val)
                tree.left = self.mergeTrees(root1.left ,root2.left)
                tree.right =  self.mergeTrees(root1.right ,root2.right)
                return tree
            else :
                 return root1 or root2

        
# def (self)===> self가 뭐야    
        
#         None 일때 처리하는게 어렵더라..
# 쉬워..! 쉬운데...! 아직 개념이 확실하지 않은듯..!
# 트리 첫번째 문제라 .. 근데 linked list 할 수 있었으면 크게 문제 없는 문제였는데 아직 숙달이 덜된듯
# 트리, recursive, dfs아직 부족하다
        
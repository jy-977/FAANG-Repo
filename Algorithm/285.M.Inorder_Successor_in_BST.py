# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        #return 값이 node인지 value 인지를 잘 확인...
#IDEA 1 ) iteration 217ms 5.21% / 18.9mb 22.27 less -------------------------------------
#         output =[]
#         stack , pointer = [] ,root
#         while stack or pointer : 
#             if pointer : 
#                 stack.append(pointer)
#                 pointer = pointer. left
#             else : 
#                 pointer = stack.pop()
#                 output.append(pointer)
#                 pointer = pointer.right
        
#         for idx in range(len(output)) : 
#             if output[idx].val == p.val : 
#                 if( idx + 1 < len(output)) : return output[idx+1]
#                 else : return None
        

        #REVIEW : 
        #inorder 의 전형적인 접근방식으로 문제를 계속 풀다보니까 쉽고 빠르긴한데
        #퍼포먼스가 안나온다. 새로운 방식으로 접근하는 연습해야함
        
# # solution ITERATION no list 76ms 93.55% faster /18.8 66.03 less--------------------------------------------
        output = None 
        while root : 
            if p.val >= root.val :
                root = root.right
            else : 
                output = root
                root = root.left
        return output
    
        #REVIEW :
        #코드는 훨씬 간단한데 훨씬 빠르다
        #내가 원리 이해를 못하고 풀었던게 이해되는부분
        #외우자 이코드는 
        # while root : 
        #     if p.val >= root.val :
        #         root = root.right
        #     else : 
        #         root= root.left
        #기본적으로  BST Search 코드
        
        #1) BST 순회코드 
        
            #1-1) recursion
            # def inorder (root) :
            #     return inorder(root.left) + [root.val] + inorder(root.right) if root else[]

            #1-2 ) iteration : 
            # output = []
            # stack,p =[],root
            # while stack or p : 
            #     if p : 
            #         stack.append(p.val)
            #         p = p.left
            #     else : 
            #         p = stack.pop()
            #         output.append(p.val)
            #         p = p.right
        #2) BST Search 
            # while root : 
            #     if p<root.val : 
            #         root = root.left
            #     elif p>root.val:  
            #         root =root.right
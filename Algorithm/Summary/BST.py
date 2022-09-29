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
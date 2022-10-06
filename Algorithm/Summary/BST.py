 #1) BST 순회코드 
        
            #1-1) recursion
            def inorder (root) :
                return inorder(root.left) + [root.val] + inorder(root.right) if root else[]

            #1-2 ) iteration : 
            output = []
            stack,p =[],root
            while stack or p : 
                if p : 
                    stack.append(p)
                    p = p.left
                else : 
                    p = stack.pop()
                    output.append(p.val)
                    p = p.right
            # 1-3) DFS : 
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

        #2) BST Search 
            while root : 
                if p<root.val : 
                    root = root.left
                elif p>root.val:  
                    root =root.right

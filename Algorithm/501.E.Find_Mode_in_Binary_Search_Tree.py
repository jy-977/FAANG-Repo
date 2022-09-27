# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        #문제 이해 잘못함...
        #가장 자주 나오는 element 반환
        
        # #iterations
        # output =[]
        # visited =[]
        # stack, p = [], root 
        # while p or stack  : 
        #     if(p) : 
        #         stack.append(p)
        #         if(p.val in visited) : 
        #             output.append(p.val)
        #         visited.append(p.val)
        #         p = p.left
        #     else : 
        #         p = stack.pop()
        #         if(p.val in visited) :
        #            output.append(p.val)
        #         visited.append(p.val)
        #         p = p.right 
        # return output
        
        #recursion 1 : 77ms 72.73% faster / 18.6mb 17.33% less
        visited = {}
        def inorder (root,visited) : 
             if root : 
                if(root.val not in visited) : 
                    visited[root.val] = 1
                else : 
                    visited[root.val]+=1
                #     output.append(root.val)
                # visited.append(root.val)
                inorder(root.left,visited)
                inorder(root.right,visited)
        inorder(root, visited)
        print(visited)
        m = 0 
        output = []
        for node in visited : 
            if (visited[node]>m) :
                output = [node]
                m = visited[node]
            elif(visited[node]==m) : 
                output.append(node)
        return output
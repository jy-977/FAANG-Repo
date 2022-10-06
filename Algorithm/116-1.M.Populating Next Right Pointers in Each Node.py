"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        #idea  ) recursive + deque : 148ms 18.84% faster / 15.5 96.77% less
        def dfs(q) : 
            nq = deque([])
            prev = q.popleft()
            if prev : 
                nq.append(prev.left)
                nq.append(prev.right)
                for i in range(len(q)) : 
                    cur = q.popleft()
                    nq.append(cur.left)
                    nq.append(cur.right)
                    prev.next = cur
                    prev = cur
                prev.next = None
                dfs(nq)
            
            
        dfs(deque([root]))
        return root
    
    #review : 코드 더러움...
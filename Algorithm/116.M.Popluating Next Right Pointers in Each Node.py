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
#       break point
        if not(root) :  return None
        q = deque([root])
# main action                
        while q : 
            emptyNode = None
            for _ in range(len(q)) : 
                cur = q.popleft()
                cur.next , emptyNode = emptyNode, cur
                if(cur.right):
                    q.extend([cur.right, cur.left])
        return root        
        
# --------------try2-----------------------------------
#         def bfs(q,checkList, root) : 
# #         1) return condition
#             if not q : return 
# #         2) MAIN ACTION
#             print("q : ", checkList)
#             cur = q.popleft()
#             checkList.popleft()
#             print(cur.val)
# #              for문 대신에 그냥 나열
#             if(cur.left and cur.right) : 
#                 q.append(cur.right)
#                 checkList.append(cur.right.val)
#                 q.append(cur.left)
#                 checkList.append(cur.left.val)
               
             
#             if(q): 
#                 print(cur.val,"next", q[0].val)
#                 cur.next = q[0]
#             else : 
#                 print(cur.val,"next", "null")
#                 cur.next = None;
#             bfs(q,checkList, root)
#             print("out", cur.val)
            
#         q = deque();
#         checkList = deque()
#         q.append(root);
#         checkList.append(root.val)
#         bfs(q,checkList, root)
#  console...-->        
# q :  deque([1])
# 1
# 1 next 3
# q :  deque([3, 2])
# 3
# 3 next 2
# q :  deque([2, 7, 6])
# 2
# 2 next 7
# q :  deque([7, 6, 5, 4])

# ==> 중요한 차이점
# 1) 2중 loop
# while  q:
#   for _ in -:
# 2) queue의 선언
# 이 방법에서는 queue를 함수 파라미터로 전달해서 level 별로 짤리지가 않고 누적됨
# 함수 안에서 선언하면 level 별로 자를수 있다.
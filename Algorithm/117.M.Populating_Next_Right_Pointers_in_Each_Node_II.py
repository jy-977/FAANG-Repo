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
    def connect(self, root: 'Node') -> 'Node':
#         #deque , bfs ? : 88ms 51.37% fsaster / 15.3mb 49.04 %
# space complexity :O(N)
#         def dfs(q) : 
#             if q : 
#                 prev = q.popleft()
#                 if prev : 

#                     nq = deque([])
#                     if(prev.left) :nq.append(prev.left)
#                     if(prev.right) : nq.append (prev.right)
#                     for i in range(len(q)) : 
#                         cur = q.popleft()
#                         # print('prev : ', prev.val, 'cur', cur.val)
#                         if(cur.left) :nq.append(cur.left)
#                         if(cur.right) : nq.append (cur.right)
#                         prev.next,prev = cur, cur
#                     prev.next =None
#                     # print("------------------------------------")
#                     dfs(nq)
                    
            
#         dfs(deque([root]))
#         return root
 
#solution : 109ms 21.69 faster / 15.3mb less than 49.04 
# O(N) , O(N)
            if not root:
                return root

            # Initialize a queue data structure which contains
            # just the root of the tree
            Q = collections.deque([root])

            # Outer while loop which iterates over 
            # each level
            while Q:

                # Note the size of the queue
                size = len(Q)

                # Iterate over all the nodes on the current level
                for i in range(size):

                    # Pop a node from the front of the queue
                    node = Q.popleft()

                    # This check is important. We don't want to
                    # establish any wrong connections. The queue will
                    # contain nodes from 2 levels at most at any
                    # point in time. This check ensures we only 
                    # don't establish next pointers beyond the end
                    # of a level
                    if i < size - 1:
                        node.next = Q[0]

                    # Add the children, if any, to the back of
                    # the queue
                    if node.left:
                        Q.append(node.left)
                    if node.right:
                        Q.append(node.right)

            # Since the tree has now been modified, return the root node
            return root

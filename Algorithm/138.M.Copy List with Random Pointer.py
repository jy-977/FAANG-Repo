"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        #problem analysist
        
        #1. 그냥 copy 하면 되는거 아닌가 .. 뭐가 문제지
        # --> head.random이 이미 만들어 지지 않은 노드를 가리킬때.. 어떡할껀데?
        # --> head의 복사본이 분명히 필요하겠네.. --> loop 2개가 필요함
        
        #2. 나는 문제를 next따라가는걸로 풀었는데 이걸 random 따라서 복사해야되는거네.. 
        #도대체 문제 어디에서 그게 나와있음..?
        # --> 1의문을 해결하면 알수 있음 
    
    #idea1 ) loop
    
#         cur = head
#         save = 0
# #       1st loop : value, next copy    
#         while(cur) :
#             new = Node(cur.val, cur.next, None)
#             if(save==0) : save = new
#             cur = new.next
# #       2nd loop : random connect
#         cur = head
#         new = save
#         while(save) : 
#             save.random = cur.random
#             # save = save.next -->copy 가 아니라 아예 주소값을 바꿔버림
#         return new

    #idea 2) hash + loop // 32ms (98.53% FASTER) 14.9MB(83.36 LESS)
    #답안지 봄.. 
            cur = head
            hashmap = {None : None}
            #hashkey 가 node의 주소가 되는 구조.. 
            while(cur) : 
                copy = Node(cur.val)
                hashmap[cur] = copy
                cur = cur.next
                
            cur = head
            while(cur) : 
                copy =hashmap[cur]
                copy.next= hashmap[cur.next]  #복사된 객체를 여기서 연결해줘야함...
                copy.random= hashmap[cur.random]
                cur = cur.next
                
            return hashmap[head]


# --------------------------------------------------------------------------
    #어떻게 HEAD로 옮길건지? ==> 처음부터 head의 복사본으로 가지고 놀면됨 (cur)
    
    #항상 맨 앞과 맨 끝이 문제다
    # loop 으로 돌고난 후에 tail로 간 pointer를 맨 앞으로 돌리는 방법은 
    #==> 처음부터 맨 앞의 pointer을 다른데 저장해 놓는다
    
    #node pointer의 복사 original 과 copied의 주소 차이가 헷갈림.. 
  
# 10, Jul, 2022

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#      problem analysis 
      # 1) linked list? --> yes 
      # 2) time complexity : O(n)
        

# idea 1) indexing , slicing
# *** index approch is not possible on Linked List


# idea 2) 22ms, 13.8mb  
# solution
#       1.length 확인
#       2.get node
        # cnt =newcnt = 1
        # test = back = head
        # while (test.next) : 
        #     cnt +=1
        #     test = test.next
        # cnt = int(cnt/2)
        # while (newcnt <= cnt) : 
        #     back = back.next
        #     newcnt+=1
        # return back


 # idea 3) 36ms, 13.8mb
#       solution cheating
        slow = faster = head
        while (faster and faster.next ) :
            slow = slow.next
            faster = faster.next.next
        return slow





# content 
        # 파이썬 linkedlist 개념 
        # (data, pointer ) ==> (data, pointer) ==> (data, pointer) ==> (data, NULL)
        # Header : 맨처음 노드                                             Tail : 맨 마지막 노드
        
        
        #장점 : 수정시 용이, 미리할당할 필요 없음
        #단점 : 탐색시 인덱스가 안되니까 O(n)
        
#         주요 함수
#         Delaration : node1, node2 = Node(data1), Node(data2)
#         연결: node1.next = node2
#         헤드 설정 : head = node1
#         tail 설정 : add(data3)
#         출력 : while node.next:

# 이문제는 그냥 solution 봤음
# Listnode , linked list어떻게 다루는지 문법 자체를 모르는데..
# idea 1 이 더 빠른게 의외였음
        
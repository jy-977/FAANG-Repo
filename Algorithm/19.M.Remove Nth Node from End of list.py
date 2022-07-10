# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

#         problem analysis
#         1.O(n)
#         2.singly Linked List


#   idea1 ) 56ms, 13.9mb
#      1.length 첫번째 탐색 O(n)
#      2.link n-1 and n+1 두번째 탐색 O(n)
#         cnt ,idx= 1,1
#         temp =  head

# #       get length
#         while(temp.next):
#             temp = temp.next
#             cnt +=1
        
# #       initial temp & reconnect            
#         temp = head
#         if(cnt-n==0):
#             return head.next
#         while(temp.next):
#             if(idx == cnt-n) :
#                 temp.next = temp.next.next
#                 return head
#             else : 
#                 temp = temp.next
#                 idx +=1
    
#   idea 2) 45ms, 14mb solution cheating - two pointers
#       1.faster를 미리 n만큼 옮겨놓고 slow랑 같이 움직임
#       2.faster 옮길때마다 -1
        slow = faster = head
        for _ in range(n):
            faster = faster.next
        if(not faster) : 
            return head.next
        
        while (faster.next) :
            faster=faster.next
            slow = slow.next
        if(slow.next) : 
            slow.next = slow.next.next
        
        return head
            
              
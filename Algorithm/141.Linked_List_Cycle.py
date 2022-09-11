# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #problmen analysis
#         아 힌트 봐버렸다 ㅠㅠ 
#         1) O(1) memory : pointer

        # #two pointers : 56ms 94.91% faster / 17.5mb 94.36% less
        # 아 나 two pointers 잘 못하네
    
        # linked list two pointer특징 : 
        # slow  = slow. next , faster = faster.next.next
        
        if (head==None) : return False
        slow = head
        faster = head.next
        while faster and faster.next:
            if faster== slow : return True 
            slow = slow.next
            faster = faster.next.next
        return False
        #hash map
        
        
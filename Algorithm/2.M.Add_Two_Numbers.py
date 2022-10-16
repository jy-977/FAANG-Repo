# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         140ms 41.15 % faster / 14mb 42.94% less
        output = ListNode()
        op = output
        store = 0
        cur_sum =0
        while l1 or l2 : 
            cur_sum = ((l1.val if l1 else 0) + (l2.val if l2 else 0) +store)
            if(cur_sum > 9 ) : 
                store =1
                cur_sum= cur_sum%10
                
            else :
                store = 0 
            if l1 : 
                l1 = l1.next
            if l2 : 
                l2 = l2.next
            op.next =ListNode(cur_sum)
            op = op.next
        if store : 
            op.next = ListNode(store)
            

        return output.next
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        if(list1 and list2): 
            if(list1.val < list2.val) : 
                node.val = list1.val 
                node.next = self.mergeTwoLists(list1.next, list2)
            else : 
                node.val = list2.val
                node.next = self.mergeTwoLists(list1, list2.next)
            return node
        else : 
            return list1 or list2
        
#     problem analysis
# 1) recursive


# recursive 특수 자료형 공식 (list, tree )
# 1)파라미터 둘다 있는지 확인
#     1-1) self.함수 (parameter1, parameter2)
#     1-2) return parameter1 or return parameter 2
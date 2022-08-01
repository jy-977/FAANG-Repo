# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# 1. problem analysis
# linked list
# recursive


# idea 1 : linked list ==not work...

# recursive list 공식 확인!!
# if(par1 and par2 ) :
#     if(condition1 ) :  self.func(par1, par2)
#     else : self.func(par1, par2)
#     return node
# else : return par1 or par2
          
        # def rev(cur, reversedList) : 
        #     if(cur == None) :
        #         print(reversedList)
        #         return reversedList
        #     else : 
        #         newList = ListNode(cur.val)
        #         newList.next = reversedList
        #         print("newList",newList )
        #         rev(cur.next, newList)
                
        # return self.rev(head,None)
                


#idea2 : same 58ms 21.3MB
class Solution:
    def reverseList(self, head: Optional[ListNode], reversedList =None) -> Optional[ListNode]:
        if(head ==None) : return reversedList
        else : 
            newList = ListNode(head.val)
            newList.next = reversedList
            return self.reverseList(head.next, newList)


# 리스트 recursive함수 만드는 방법 익히기
# self..!!
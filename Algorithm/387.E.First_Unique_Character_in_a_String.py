from collections import deque
class Solution:
    def firstUniqChar(self, s: str) -> int:
#         #idea 1 ) hash - 270ms 20.93 % fsater / 13.7mb 99.98 less
#         hm ={}
#         for c in s : 
#             if(c not in hm) : 
#                 hm[c]=1
#             else : 
#                 hm[c]+=1
#         for i in range(len(s)):
#             if(hm[s[i]] ==1) : return i
#         return -1
#     #쉬운문제들인데 왜 한참 헤맸지? 이해안돼...


#   solution 2) count 내장함수 이용 - 66ms 98.20 faster / 14.1 mb 95.32 % less
        ss =set(s)
        stack = []
        print(ss)
        for c in ss:
            if(s.count(c)==1):
                stack.append(s.index(c))
        return min(stack) if len(stack)>0 else -1
class Solution:
    def reverseWords(self, s: str) -> str:

# problem analysis
# 1) two pointers?
# 2) string control


# idea 1
# two pointers & [::-1]
#         left, right =0,0
#         reversed_s = ''
#         for i in range(len(s)) :
# #           break 조건
#             if(i==len(s)-1) : 
#                 right = i
#                 reversed_s = reversed_s+s[right:left-1:-1]
#                 print("left", left, "right", right, "reversed", reversed_s)
#                 return reversed_s
#             if(s[i+1]==' ') : 
#                 right = i
#                 reversed_s=reversed_s+s[right:left-1:-1]+' '
#                 print("left", left, "right", right, "reversed", reversed_s)
#                 left = i+2
              
#             print(reversed_s)
        
        

# idea 2 내장함수 사용 
#           문자열 reverse : s.reverse()
#           리스트 reverse : reversed(list)
#           문자열 나누기 : s.split() --> 리스트 출력
#           리스트 문자열로 합치기 (구분자).(리스트)
# 
            rs = s[::-1]
            # return(' ').join(list(reversed(rs.split())))'
            return(' ').join(list(reversed(rs.split())))